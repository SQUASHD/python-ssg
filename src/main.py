import os
import shutil

from markdown_processing import markdown_to_html


def clear_directory(directory_path: str) -> None:
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
    os.makedirs(directory_path)


def copy_directory(walk_dir_path: str, target_dir_path: str) -> None:
    for root, dirs, files in os.walk(walk_dir_path):
        for dir in dirs:
            os.makedirs(os.path.join(target_dir_path, dir), exist_ok=True)
        for file in files:
            relative_path = os.path.relpath(root, walk_dir_path)
            shutil.copyfile(
                os.path.join(root, file),
                os.path.join(target_dir_path, relative_path, file),
            )


def extract_title(file_path: str) -> str:
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("# "):
                return line[2:].strip()
    raise ValueError("No title found in file")


def generate_page(from_path: str, template_path: str, to_path: str) -> None:
    print(f"Generating page from {from_path} to {to_path}")

    with open(from_path, "r") as from_file, open(
        template_path, "r"
    ) as template_file, open(to_path, "w") as to_file:
        markdown_content = from_file.read()

        for line in template_file:
            if line.strip() == "{{ Title }}":
                to_file.write(extract_title(from_path))
            elif line.strip() == "{{ Content }}":
                to_file.write(markdown_to_html(markdown_content))
            else:
                to_file.write(line)


def process_markdown_files(
    source_dir: str, template_path: str, target_dir: str
) -> None:
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".md"):
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                target_file_path = os.path.join(
                    target_dir, relative_path, os.path.splitext(file)[0] + ".html"
                )
                os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
                generate_page(source_file_path, template_path, target_file_path)


def main():
    source_markdown_dir = "./content"
    template_path = "./template.html"
    public_dir = "./public"
    static_dir = "./static"

    clear_directory(public_dir)
    copy_directory(static_dir, public_dir)
    process_markdown_files(source_markdown_dir, template_path, public_dir)


if __name__ == "__main__":
    main()
