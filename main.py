import os
import shutil


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


def main():
    clear_directory("./public")
    copy_directory("./static", "./public")


if __name__ == "__main__":
    main()
