import shutil
from textnode import TextNode, TextType
import os

def main() -> None:
    shutil.rmtree("public/")
    os.mkdir("public/")
    copy_static_and_push("static/" , "public/")
    
def copy_static_and_push(copy_dir, dest_dir):
    files = os.listdir(copy_dir)
    for file in files:
        if os.path.isfile(os.path.join(copy_dir, file)):
            shutil.copy(os.path.join(copy_dir, file), dest_dir)
        else:
            os.mkdir(os.path.join(dest_dir,file))
            copy_static_and_push(os.path.join(copy_dir, file), os.path.join(dest_dir,file))



    
    
if __name__ == "__main__":
    main()
