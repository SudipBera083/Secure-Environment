import os
import random
from tkinter import *
root = Tk()
root.title("Media Player")
root.geometry("300x400")


def music():
    music_dir = '.\music'
    songs = os.listdir(music_dir)
    data = random.randint(0, len(songs) - 1)
    os.startfile(os.path.join(music_dir, songs[data]))
    # s.playSong()


Label(root, text="Music Player", font="lucida 15 bold").pack()

# USING GIF IN THE  FRONT
frameCnt = 30
frames = [PhotoImage(file='./src/music1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
# ==================================


Button(root, text="play", command=music).pack()
root.mainloop()