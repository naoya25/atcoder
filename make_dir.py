# makefile専用のディレクトリ作成用のスクリプト
# make {dir_name}

import os
import sys

FILE_TEMPLATE = """
def main():
    return


if __name__ == "__main__":
    main()

"""


def create_files():
    dir_name = sys.argv[1]
    files = ["a.py", "b.py", "c.py", "d.py", "e.py", "f.py", "g.py"]

    dir_path = os.path.join("ABC", dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print(f"Directory '{dir_path}' already exists.")
        return
    for file in files:
        file_path = os.path.join(dir_path, file)
        with open(file_path, "w") as f:
            f.write(FILE_TEMPLATE)
        print(f"Created: {file_path}")


if __name__ == "__main__":
    create_files()
