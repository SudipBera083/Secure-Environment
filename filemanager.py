from tkinter import *
import os
from PIL import Image,ImageTk


def e_drive():
    e_data = os.listdir("E:/")
    l.delete(0,END)
    l.update()
    for i in e_data:
        l.insert(END,i)
    


def f_drive():
    e_data = os.listdir("F:/")
    l.delete(0,END)
    l.update()
    for i in e_data:
        l.insert(END,i)



def g_drive():
    e_data = os.listdir("G:/")
    l.delete(0,END)
    l.update()
    for i in e_data:
        l.insert(END,i)


root = Tk()
root.geometry("855x500")
root.maxsize(855,500)
root.minsize(855,500)
root.title("CWBH--File Manager")
root.configure(bg="black")

Label(root,text="Welcome to File Manager",fg="white",bg="black",font="lucida 25 bold").pack()
data = os.listdir("C:/")

l = Listbox(root,bg="black",fg="white",font="lucida 10")
l.pack(side=LEFT,fill=Y)


for i in data:
    l.insert(END,i)



f = Frame(root,bg="black")
f.pack(fill=X,anchor="n",padx=100,pady=100)


photo = PhotoImage(file=".\src\disk.png")

l1 = Label(f, image=photo)
l1.pack()
l1.image =photo
l1.grid(row=0,column=0)

Button(f,text="New Volume(E:)",fg="white",bg="black",command=e_drive).grid(row=1,column=0,padx=50,pady=10)

l2 = Label(f, image=photo)
l2.grid(row=0,column=1)
l2.image =photo

Button(f,text="Local Disk(F:)",fg="white",bg="black",command=f_drive).grid(row=1,column=1,padx=40)

l3 = Label(f, image=photo)
l3.grid(row=0,column=2)
l3.image =photo
Button(f,text="New Volume(G:)",fg="white",bg="black",command=g_drive).grid(row=1,column=2,padx=40)


Label(root,text="You can not access this Folders as we are working on it.",bg="black",fg="white",font="lucida 15").pack()


root.mainloop()