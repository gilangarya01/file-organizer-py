import argparse
import os
import shutil

# Function untuk membuat folder jika folder tidak ada
def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        print(f"Folder '{folder_path}' sudah ada.")

# Function untuk memindahkan file ke folder
def organize_file(file_path, category_folder):
    shutil.move(file_path, category_folder)

# Function untuk mengatur file sesuai dengan extension file
def organize_files(dir_path):
    # Kategori folder
    category_folders = {
        "Documents": [".docx", ".pdf"],
        "Musics": [".mp3", ".wav"],
        "Images": [".png", ".jpg"],
        "Videos": [".mp4", ".avi"],
        "Others": [],
    }

    # Buat folder kategori jika tidak ada
    for folder in category_folders:
        create_folder(os.path.join(dir_path, folder))

    # Atur file sesuai dengan extension file
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)

        if os.path.isfile(file_path):
            name, extension = os.path.splitext(filename)

            # Memindahkan file sesuai dengan kategorinya
            for category, extensions in category_folders.items():
                if extension.lower() in extensions:
                    organize_file(file_path, os.path.join(dir_path, category))
                    break
            else:
                # Jika file tidak sesuai pindahkan ke folder Others
                organize_file(file_path, os.path.join(dir_path, "Others"))

def main():
    parser = argparse.ArgumentParser(description="Atur file berdasarkan ekstensinya.")
    parser.add_argument("dir_path", help="Path dari direktori yang berisi file yang akan diatur.")
    args = parser.parse_args()

    organize_files(args.dir_path)
    print("File berhasil diatur.")

if __name__ == "__main__":
    main()
