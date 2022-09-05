import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


def Widgets():
    Baslik_label = Label(root, text="MP3 Dönüştürücü",
                         padx=15,
                         pady=15,
                         font="SegoeUI 14",
                         bg="#833471",
                         fg="Black")
    Baslik_label.grid(row=1,
                      column=1,
                      pady=10,
                      padx=5,
                      columnspan=3)

    link_label = Label(root,
                       text="YouTube link :",
                       bg="#FDA7DF",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    yer_label = Label(root,
                      text="Yer :",
                      bg="#FDA7DF",
                      pady=5,
                      padx=5)
    yer_label.grid(row=3,
                   column=0,
                   pady=5,
                   padx=9)

    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#B53471",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Video'yu İndir",
                        command=Download,
                        width=20,
                        bg="#FDA7DF",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)


def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Video Kaydedildi")

    download_Path.set(download_Directory)


def Download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)

    videoStream = getVideo.streams.first()

    videoStream.download(download_Folder)

    messagebox.showinfo("BAŞARILI'",
                        "Videonuz kaydedildi..\n"
                        + download_Folder)


root = tk.Tk()

root.geometry("520x280")

root.title("Youtube video indirici")
root.config(background="#833471")

video_Link = StringVar()
download_Path = StringVar()

Widgets()

root.mainloop()