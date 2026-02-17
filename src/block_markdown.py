from enum import Enum

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

    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    
    if block.startswith(("######", "#####", "####", "###", "##", "#")):
        return BlockType.HEADING
    
    lines = block.split("\n")
    if block[0] == ">":
        for line in lines:
            if line[0] != ">":
                return type
        return BlockType.QUOTE
    if block.startswith(("- ")):
        for line in lines:
            if not line.startswith("- "):
                return type
        return BlockType.UNORDEREDLIST
    
    if block.startswith(("1. ")):
        for i in range(1, len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return type
             
        return BlockType.ORDEREDLIST

    return type
