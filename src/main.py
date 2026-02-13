from textnode import TextNode, TextType


def main():

    text_node = TextNode("testing text", TextType.LINK, "https://www.boot.dev")
    print(text_node)


main()
