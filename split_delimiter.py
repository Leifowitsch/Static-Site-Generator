import re
from src.textnode import TextNode, TextType
delimiters = {
    "bold" : "**",
    "italic" : "_",
    "code" : "`"
    }
     

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_art = text_type
    if delimiter not in delimiters.values():
        raise ValueError("Delimiter ist nicht Valide")
    if text_type == TextType.plain:
        return old_nodes
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.plain:
            new_nodes.append(node)
            continue
        anfang = True
        split_punkt = 0
        ende = len(node.value) -1
        for index in range(len(node.value)):

            if index !=0 and node.value[index]+node.value[index-1] == delimiter:
                continue


            # Das hier ist für alle delimiter die aus einem Zeichen bestehen
            if node.value[index] == delimiter:
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
            elif node.value[index]+node.value[index+1] == delimiter:
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
        bild_nummer = 0
        split_punkt = 0
        anfang = True
        if node.text_type == TextType.images:
            new_nodes.append(node)
            continue
        #if "!"  not in node.value or "(" not in node.value or "[" not in node.value:
         #   raise ValueError("Ungültiger Text für ein Bild oder ungültiges Format - Richtiges Format ist bspw.: This is text with a image ![image](https://www.boot.dev)")
        alt_text_and_link = extract_markdown_images(node.value)
        for index in range(len(node.value)):
            if node.value[index] == "!" or node.value[index] == ")":
                if anfang is True:
                    new_nodes.append(TextNode(value=node.value[split_punkt:index], text_type=TextType.plain))
                    anfang = False
                    split_punkt = index +1

                elif anfang is not True:
                    new_nodes.append(TextNode(value=alt_text_and_link[bild_nummer][0], url=alt_text_and_link[bild_nummer][1], text_type=TextType.images))
                    anfang = True 
                    split_punkt = index +1
                    bild_nummer += 1
    return new_nodes

def main():
    node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.plain)
    new_nodes = split_nodes_image([node])
    for node in new_nodes:
        print(node)
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
    test = text.split("![alt_text_and_link[0][0]](alt_text_and_link[0][1])", 1)
    print(test)


main()

                






