from tkinter import *

def click(Event):
    global scvalue
    text =  Event.widget.cget("text")
    # print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
               value  = eval(scvalue.get())
            except Exception as e:
                value= "Error"
                print(e)
        
        scvalue.set(value)
        screen.update()

    elif text =="C" or text=="AC":
        scvalue.set("")
        screen.update()
    
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()


root = Tk()
root.geometry("340x430")
root.maxsize(340,430)
root.minsize(340,430)
root.title("Smart Calculator")
root.wm_iconbitmap(".\src\icon.ico")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root,bg = "black",fg = "white",textvariable=scvalue, font = "lucida 40 bold", borderwidth=5)
screen.pack(fill=X, ipadx =10, ipady=10)

f  = Frame(root,bg= "black")

b = Button(f, text="7",font="lucida 25 bold", padx=5, pady=5)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)


b = Button(f, text="8",font="lucida 25 bold", padx=5, pady=5)
b.pack(side = LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="9",font="lucida 25 bold", padx=5, pady=5)
b.pack(side = LEFT, padx=5 ,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+",font="lucida 25 bold", padx=5, pady=5)
b.pack(side=LEFT, padx=5 ,pady=5)
b.bind("<Button-1>", click)

b4 = Button(f, padx=6, pady=5, text="%", font="lucida 25 bold")
b4.pack(side=LEFT, padx=5, pady=5)
b4.bind("<Button-1>", click)


f.pack()



f1  = Frame(root,bg= "black")

b1 = Button(f1, padx=8, pady=5, text="4", font="lucida 25 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b1 = Button(f1, padx=8, pady=5, text="5", font="lucida 25 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b1 = Button(f1, padx=8, pady=5, text="6", font="lucida 25 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b1 = Button(f1, padx=8, pady=5, text="-", font="lucida 25 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b4 = Button(f1, padx=8, pady=5, text=".", font="lucida 25 bold")
b4.pack(side=LEFT, padx=5, pady=5)
b4.bind("<Button-1>", click)


f1.pack()



f2  = Frame(root,bg= "black")

b2 = Button(f2, padx=5, pady=5, text="1", font="lucida 25 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b2 = Button(f2, padx=5, pady=5, text="2", font="lucida 25 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b2 = Button(f2, padx=5, pady=5, text="3", font="lucida 25 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b2 = Button(f2, padx=5, pady=5, text="*", font="lucida 25 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b4 = Button(f2, padx=5, pady=5, text="00", font="lucida 25 bold")
b4.pack(side=LEFT, padx=5, pady=5)
b4.bind("<Button-1>", click)


f2.pack()



f3  = Frame(root,bg= "black")

b3 = Button(f3, padx=5, pady=5, text="0", font="lucida 25 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f3, padx=11, pady=5, text="/", font="lucida 25 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f3, padx=5, pady=5, text="=", font="lucida 25 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f3, padx=5, pady=5, text="C", font="lucida 25 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b4 = Button(f3, padx=1, pady=5, text="AC", font="lucida 25 bold")
b4.pack(side=LEFT, padx=5, pady=5)
b4.bind("<Button-1>", click)


f3.pack()









root.mainloop()