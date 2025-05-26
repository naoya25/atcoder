# makefile専用のディレクトリ作成用のスクリプト
# make {dir_name}

import os
import sys
import subprocess

FILE_TEMPLATE = """def main():
    return


if __name__ == "__main__":
    main()

"""


def create_files():
    dir_name = sys.argv[1]
    files = ["a.py", "b.py", "c.py", "d.py", "e.py", "f.py", "g.py"]
    files_dart = ["a.dart", "b.dart", "c.dart", "d.dart", "e.dart", "f.dart", "g.dart"]

    dir_path = os.path.join("./ABC", dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print(f"Directory '{dir_path}' already exists.")
        return

    is_dart = "dart" in dir_name
    target_files = files if not is_dart else files_dart

    for t_file in target_files:
        file_path = os.path.join(dir_path, t_file)
        with open(file_path, "w") as f:
            f.write(FILE_TEMPLATE if not is_dart else "")
        print(f"Created: {file_path}")

    open_cmd = ["cursor", os.path.join(dir_path, target_files[0]), "./input.txt"]
    subprocess.run(open_cmd)


if __name__ == "__main__":
    create_files()
