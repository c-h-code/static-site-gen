def markdown_to_blocks(markdown):
    blocks = [line.strip() for line in markdown.split("\n\n")]
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks
