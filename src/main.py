import shutil
from block_markdown import extract_title, markdown_to_html_node
from textnode import TextNode, TextType
import os

def main() -> None:
    shutil.rmtree("public/")
    os.mkdir("public/")
    copy_static_and_push("static/" , "public/")
    generate_page("content/index.md", "template.html", "public/index.html")
    
def copy_static_and_push(copy_dir, dest_dir):
    files = os.listdir(copy_dir)
    for file in files:
        if os.path.isfile(os.path.join(copy_dir, file)):
            shutil.copy(os.path.join(copy_dir, file), dest_dir)
        else:
            os.mkdir(os.path.join(dest_dir,file))
            copy_static_and_push(os.path.join(copy_dir, file), os.path.join(dest_dir,file))



def generate_page(from_path,template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path,"r") as f:
        markdown = f.read()
    with open(template_path,"r") as f:
        template = f.read()
    html = markdown_to_html_node(markdown)
    html = html.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path:
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)

    


         
    
    
if __name__ == "__main__":
    main()
