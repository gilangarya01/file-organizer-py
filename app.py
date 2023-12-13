import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import os
import shutil

def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        print(f"Folder '{folder_path}' sudah ada.")

def organize_file(file_path, category_folder):
    shutil.move(file_path, category_folder)

def organize_files(dir_path, category_folders):
    for folder in category_folders:
        create_folder(os.path.join(dir_path, folder))

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)

        if os.path.isfile(file_path):
            name, extension = os.path.splitext(filename)
            for category, extensions in category_folders.items():
                if extension.lower() in extensions:
                    organize_file(file_path, os.path.join(dir_path, category))
                    break
            else:
                organize_file(file_path, os.path.join(dir_path, "Others"))

    CTkMessagebox(message="File berhasil diatur.", icon="check", option_1="OK")

def browser_folder():
    directory = ctk.filedialog.askdirectory()
    if directory.strip():
        category_folders = {
            "Documents": [".docx", ".pdf"],
            "Musics": [".mp3", ".wav"],
            "Images": [".png", ".jpg"],
            "Videos": [".mp4", ".avi"],
            "Others": [],
        }
        organize_files(directory, category_folders)
    else:
        CTkMessagebox(message="Path folder tidak tersedia.", icon="cancel", option_1="OK")

app = ctk.CTk()
app.geometry("400x240")
app.title("File Organizer")

button = ctk.CTkButton(master=app, text="Cari Folder", command=browser_folder)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
