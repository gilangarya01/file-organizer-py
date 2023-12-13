import customtkinter as ctk
import utils

def main():
    app = ctk.CTk()
    app.geometry("400x240")
    app.title("File Organizer")

    button = ctk.CTkButton(master=app, text="Cari Folder", command=utils.browser_folder)
    button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    app.mainloop()

if __name__ == "__main__":
    main()