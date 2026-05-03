# makefile専用のディレクトリ作成用のスクリプト
# make {dir_name}

import os
import subprocess
import sys

PY_TEMPLATE = """def main():
    return


if __name__ == "__main__":
    main()

"""

RS_TEMPLATE = """use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_ascii_whitespace();
}
"""


def cargo_toml_content(name, base_names):
    bins = "\n".join(f'\n[[bin]]\nname = "{n}"\npath = "{n}.rs"' for n in base_names)
    return f'[package]\nname = "{name}"\nversion = "0.1.0"\nedition = "2021"\n{bins}\n'


def create_files():
    dir_name = sys.argv[1]
    dir_path = os.path.join("./ABC", dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print(f"Directory '{dir_path}' already exists.")
        return

    parts = dir_name.rsplit("_", 1)
    ext = parts[1] if len(parts) == 2 else "py"
    base_names = ["a", "b", "c", "d", "e", "f", "g"]

    if ext == "rs":
        target_files = [f"{name}.{ext}" for name in base_names]
        for t_file in target_files:
            file_path = os.path.join(dir_path, t_file)
            with open(file_path, "w") as f:
                f.write(RS_TEMPLATE)
            print(f"Created: {file_path}")
        cargo_toml = os.path.join(dir_path, "Cargo.toml")
        package_name = "abc" + parts[0].lower()
        with open(cargo_toml, "w") as f:
            f.write(cargo_toml_content(package_name, base_names))
        print(f"Created: {cargo_toml}")
        first_file = os.path.join(dir_path, target_files[0])
    else:
        target_files = [f"{name}.{ext}" for name in base_names]
        for t_file in target_files:
            file_path = os.path.join(dir_path, t_file)
            with open(file_path, "w") as f:
                f.write(PY_TEMPLATE if ext == "py" else "")
            print(f"Created: {file_path}")
        first_file = os.path.join(dir_path, target_files[0])

    open_cmd = ["code", first_file, "./input.txt"]
    subprocess.run(open_cmd)


if __name__ == "__main__":
    create_files()
