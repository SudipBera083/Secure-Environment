from tkinter import *
import datetime

root = Tk()
root.title("CWBH -- Clock")
root.geometry("450x500")
root.configure(bg="black")

Label(root, text="CLOCK", fg="white",bg="black", font="lucida 20 bold").pack()
Label(root,text="Powered by Code With BonggoHriday",bg="black",fg="white",font="lucida 10 ").pack(padx=10)

raw_data = str(datetime.datetime.now())
purified_data = raw_data.split(" ")
date1 = purified_data[0]
time = purified_data[1]
time1 = time.split(".")
time2 = time1[0]


can_widget = Canvas(root,bg="black")
can_widget.pack(pady=50)
can_widget.create_oval(0,10,15,20)
Label(can_widget, text=time2,bg="black",fg="white", font="lucida 40 bold").pack(pady=50)

Label(root,text="Date: ",fg="white",bg="black", font="lucida 15 bold").pack(side=LEFT, anchor="n",padx=100)
Label(root,text=date1,fg="white",bg="black", font="lucida 15 bold").pack(side=LEFT,anchor="n")


# note = """This GUI is only for testing purpose."""
# Label(root,text=note,fg="white",bg="black", font="lucida 15 bold").pack(anchor="s",padx=10)


root.mainloop()