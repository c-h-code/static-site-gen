from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered_list"
    ORDEREDLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = [line.strip() for line in markdown.split("\n\n")]
    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(block):
    type = BlockType.PARAGRAPH

    if not block:
        return type

    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    
    if block.startswith(("###### ", "##### ", "#### ", "### ", "## ", "# ")):
        return BlockType.HEADING
    
    lines = block.split("\n")
    

    if block[0] == ">":
        for line in lines:
            if not line.startswith (">"):
                return type

        return BlockType.QUOTE
    
    if block.startswith("- ") or block.startswith("* "):
        if block.startswith("- "):
            for line in lines:
                if not line.startswith("- "):
                    return type

        if block.startswith("* "):
            for line in lines:

                if not line.startswith("* "):
                    return type

        return BlockType.UNORDEREDLIST
    
    if block.startswith("1. "):

        for i in range(1, len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return type
             
        return BlockType.ORDEREDLIST

    return type

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    
    for block in blocks:
        
        block_type = block_to_block_type(block)
        match (block_type):
            case BlockType.PARAGRAPH:
                block = block.replace("\n", " ")
                block = " ".join(block.split())
                html_node = ParentNode("p",text_to_children(block),None)

            case BlockType.HEADING:
                block = block.replace("\n", " ")
                block = " ".join(block.split())
                num_of_hashtag = len(block) - len(block.lstrip("#"))
                block = block[num_of_hashtag + 1:]
                html_node = ParentNode(f"h{num_of_hashtag}",text_to_children(block),None)

            case BlockType.QUOTE:
                block = block.lstrip(">")
                block = block.replace("\n>", " ")
                block = " ".join(block.split())
                html_node = ParentNode("blockquote",text_to_children(block),None)

            case BlockType.UNORDEREDLIST:
                lines = block.split("\n")
                list_nodes = []
                for line in lines:
                    line = line[2:]
                    list_nodes.append(ParentNode("li",text_to_children(line),None))
                
                html_node = ParentNode("ul",list_nodes,None)
            
            case BlockType.ORDEREDLIST:
                lines = block.split("\n")
                list_nodes = []
                for line in lines:
                    line = line.split(". ",1)[1]
                    list_nodes.append(ParentNode("li",text_to_children(line),None))
                
                html_node = ParentNode("ol",list_nodes,None)

            case BlockType.CODE:
                block = block[3:-3].strip()
                code_text_node = TextNode(block,"text")
                code_node = ParentNode("code",[text_node_to_html_node(code_text_node)])
                html_node = ParentNode("pre", [code_node], None)
            
                


            
        
        html_nodes.append(html_node)   
        
    return ParentNode("div", html_nodes)
                
                



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))

    
    return html_nodes
    





