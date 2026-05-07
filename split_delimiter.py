import re
from src.textnode import TextNode, TextType
delimiters = {
    "**" : "bold",
    "_" : "italic",
    "`" : "code"
    }
     

def split_nodes_delimiter(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.plain:
            new_nodes.append(node)
            continue
        anfang = True
        split_punkt = 0
        ende = len(node.value) -1
        for index in range(len(node.value)):

            if index !=0 and node.value[index]+node.value[index-1] in delimiters.keys():
                continue


            # Das hier ist für alle delimiter die aus einem Zeichen bestehen
            if node.value[index] in delimiters.keys():
                delimiter_type = delimiters[node.value[index]]
                text_art = TextType[delimiter_type]
                if anfang is True:
                    new_nodes.append(TextNode(node.value[split_punkt:index], text_type=TextType.plain))
                    split_punkt = index + 1
                    anfang = False
                elif anfang is not True:
                    new_nodes.append(TextNode(value=node.value[split_punkt:index], text_type=text_art))
                    split_punkt = index +1
                    anfang = True
                continue


            # Wenn der Index den letzten char erreicht hat und split nicht gleich dem Index +1 ist bedeutet das, dass der letzte Teil des Textes plain sein muss und split ist entweder der anfang weil es nie gesplitet wurde
            # oder split ist der letzte punkt wo der Text gesplitet wurde. also wo die schriftart aufgehört hat 
            if index == ende and split_punkt != index +1 and split_punkt != index +2:
                new_nodes.append(TextNode(node.value[split_punkt:index +1], text_type=TextType.plain)) 
                break

            # Das hier ist für Bold, da der delimitor für bold aus 2 zeichen besteht!, bzw für alle Delimiter aus 2 Zeichen
            elif node.value[index]+node.value[index+1] in delimiters.keys():
                delimiter_type = delimiters[node.value[index]+node.value[index+1]]
                text_art = TextType[delimiter_type]
                if anfang is True:
                    new_nodes.append(TextNode(node.value[split_punkt:index], text_type=TextType.plain))
                    split_punkt = index +2
                    anfang = False
                elif anfang is not True:
                    new_nodes.append(TextNode(value=node.value[split_punkt:index], text_type=text_art))
                    split_punkt = index +2
                    anfang = True
                # Falls die beiden letzen zeilen delimiter sind wollen wir abbrechen sobald das erkannt wurde weil sonst der Vergleich schauen möchte ob das letzte zeichen mit dem darauffolgendem zeichen = delimiter ist, aber
                # da es kein darauffolgendes zeichen gibt würde das programm abstürzen.
                if index == len(node.value)-2:
                    break

    return new_nodes



def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        alt_text_and_link = extract_markdown_images(node.value)
        if alt_text_and_link is None or alt_text_and_link == []:
            new_nodes.append(node)
            continue
        text_to_split = node.value
        if node.text_type == TextType.images:
            new_nodes.append(node)
            continue
        for image_num in range(len(extract_markdown_images(node.value))):
            text_splitted = text_to_split.split(f"![{alt_text_and_link[image_num][0]}]({alt_text_and_link[image_num][1]})",1)
            if text_splitted[0] != "":
                new_nodes.append(TextNode(value=text_splitted[0], text_type=TextType.plain))
            text_to_split = text_splitted[1]
            new_nodes.append(TextNode(value=alt_text_and_link[image_num][0], url=alt_text_and_link[image_num][1], text_type=TextType.images))

    return new_nodes
    
def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        alt_text_and_link = extract_markdown_links(node.value)
        if alt_text_and_link is None or alt_text_and_link == []:
            new_nodes.append(node)
            continue
        text_to_split = node.value
        if node.text_type == TextType.links:
            new_nodes.append(node)
            continue
        for link_num in range(len(extract_markdown_links(node.value))):
            text_splitted = text_to_split.split(f"[{alt_text_and_link[link_num][0]}]({alt_text_and_link[link_num][1]})",1)
            if text_splitted[0] != "":
                new_nodes.append(TextNode(value=text_splitted[0], text_type=TextType.plain))
            text_to_split = text_splitted[1]
            new_nodes.append(TextNode(value=alt_text_and_link[link_num][0], url=alt_text_and_link[link_num][1], text_type=TextType.links))
    return new_nodes


def text_to_textnodes(text):
    new_nodes = []
    adding_nodes= []
    node = TextNode(value=text, text_type=TextType.plain)
    #print(split_nodes_delimiter([node]))
    new_nodes.extend(split_nodes_image([node]))
    new_nodes.extend(split_nodes_links([node]))
    print(new_nodes)
    
text_to_textnodes("This is a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")

                






