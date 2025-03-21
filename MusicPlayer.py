# wrote by amirttl7
#GITHUB: https://github.com/amirttl7/musicplayer


import tkinter as tk
from tkinter import filedialog
import pygame as pg
import os




# Initialize Pygame mixer in case you'll use it for playback later
pg.mixer.init()

# Create the main application window
root = tk.Tk()
root.title("MUSIC PLAYER")
root.geometry("600x400")
root.resizable(False, False)

#--------------------------------------------------

statuse = tk.StringVar()
pg.init()
pg.mixer.init()

#-------------button function-----------------------

def playsong():
    showsongname.config(state="normal")
    showsongname.delete("1.0","end")
    showsongname.insert("1.0",playlist.get("active"))
    showsongname.config(state="disabled")
    
    statuse.set("playing")
    pg.mixer.music.load(playlist.get("active"))
    pg.mixer.music.play()

def stopsong():
    statuse.set("stoped")
    pg.mixer.music.stop()

def unpausesong():
    statuse.set("unpausing")
    pg.mixer.music.unpause()

def pausesong():
    statuse.set("pausing")
    pg.mixer.music.pause()







# --------------------------- Song Playlist Frame ---------------------------
songplaylistframe = tk.LabelFrame(root, text="Play List", bg="black", fg="white", bd=4, font=("Arial", 10))
songplaylistframe.place(x=10, y=0, width=580, height=208)

scrollbar = tk.Scrollbar(songplaylistframe, orient="vertical" , )
scrollbar.pack(fill="y", side="right")

playlist = tk.Listbox(
    songplaylistframe,
    bg="silver",
    fg="red",
    font=("Helvetica", 10),
    selectmode="single",
    selectbackground="black",
    height=100,
    yscrollcommand=scrollbar.set

)
playlist.pack(fill="both")
scrollbar.config(command=playlist.yview)

# --------------------------- Song Track Frame ---------------------------
songtrackframe = tk.LabelFrame(root, text="SongTrack", bg="black", fg="white", bd=4, font=("Arial", 10) ,)
songtrackframe.place(x=10, y=212, width=580, height=90)

showsongname = tk.Text(songtrackframe, bg="white", fg="red", width=50, height=1, state="disabled")
showsongname.grid(row=0, column=0, padx=17, pady=13)

showstatuse = tk.Label(songtrackframe, bg="white", fg="red", width=15  ,textvariable=statuse)
showstatuse.grid(row=0, column=1)

# ----------------------- Function to Load Songs -----------------------
def load_songs_from_folder(folder_path):
    """
    Loads any songs with allowed extensions from the given folder into the playlist.
    """
    allowed_exts = ('.mp3', '.wav', '.ogg', '.flac')
    # List all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file has a valid extension (case-insensitive)
        if filename.lower().endswith(allowed_exts):
            full_path = os.path.join(folder_path, filename)
            playlist.insert(tk.END, full_path)

# ----------------------- "Add Folder" Button Callback -----------------------
def add_folder():
    # Open a dialog to select a directory
    folder_path = filedialog.askdirectory(title="Select Music Folder")
    if folder_path:
        load_songs_from_folder(folder_path)

# --------------------------- Control Panel ---------------------------
ctrpanel = tk.LabelFrame(root, text="ControlPanel", bg="black", fg="white", bd=4, font=("Arial", 10), padx=17)
ctrpanel.place(x=10, y=308, width=580, height=90)

playbtn = tk.Button(ctrpanel, text="Play", width=13,command=playsong)
playbtn.grid(row=0, column=0, pady=17, padx=3.4)

stopbtn = tk.Button(ctrpanel, text="Stop", width=13,command=stopsong)
stopbtn.grid(row=0, column=1, pady=17, padx=3.4)

unpausebtn = tk.Button(ctrpanel, text="Unpause", width=13,command=unpausesong)
unpausebtn.grid(row=0, column=2, pady=17, padx=3.4)

pausebtn = tk.Button(ctrpanel, text="Pause", width=13,command=pausesong)
pausebtn.grid(row=0, column=3, pady=17, padx=3.4)

# "Add Folder" button to add songs from a new folder
addfolderbtn = tk.Button(ctrpanel, text="Add Folder", width=13, command=add_folder)
addfolderbtn.grid(row=0, column=4, pady=17, padx=3.4)

# ------------------- Load Default Folder at Startup -------------------
default_folder = r"E:\musicand pic\music pop"
if os.path.exists(default_folder):
    load_songs_from_folder(default_folder)
else:
    print(f"Default folder not found: {default_folder}")

# Start the tkinter main loop
root.mainloop()