import tkinter
from tkinter import*
import random
from tkinter import messagebox


answer=[
    "sex",
    "fuck",
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "delhi",
    "germany",
    "bhutan",
    "girlfriend",
    "boyfriend",

    ]
words = [
    "xes",
    "kucf",
    "npytho",
    "avaj",
    "switf",
    "canaad",
    "indai",
    "ameirac",
    "ldonon",
    "lhide",
    "gernyma",
    "tanbhu",
    "friendgirl",
    "friendboy",

    ]

num = random.randrange(0,12,1)
def Reset():
    global words, answer, num
    num = random.randrange(0,12,1)
    lbl.config(text=words[num])
    e1.delete(0,END)

def default():
    global words,answer,num
    lbl.config(text = words[num])

def Checkans():
    global words,answer,num
    var = e1.get()
    if var ==answer[num]:
        messagebox.showinfo("Success","Correct ans ")
        Reset()
    else:
        messagebox.showerror("Error","incorrect ans")
        e1.delete(0,END)



root=tkinter.Tk()

root.geometry("350x400+400+300")
root.title("jumbled")
root.configure(background="gray")

photo = PhotoImage(file="C://Users//Dhiraj kumar//Desktop//python//d.png")
w = Label(root,image=photo)
w.pack()





lbl=Label(

    root,
    text="Your text her",
    font=("vardana",18),
    bg="gray",
    fg="#ecf0f1"
)
lbl.pack(pady=30,ipady=10,ipadx=10)


ans = StringVar()
e1 = Entry(
    root,
    font = ("verdana",18),
    textvariable =ans,
    bg="#7f8c8d"
)
e1.pack(ipady=5,ipadx=5)

btncheak = Button(
    root,
    text = "Check",
    font =("comic sans ms",16),
    width = "16",
    fg = "#CAD3C8",
    background = "#3B3B98",
    relief = GROOVE,
    command = Checkans,
)
btncheak.pack(pady=40)


btncheak = Button(
    root,
    text = "Reset",
    font =("comic sans ms",16),
    width = "16",
    fg = "#6D214F",
    background = "#58B19F",
    relief = GROOVE,
    command = Reset,
)
btncheak.pack(pady=10)

default()

root.mainloop()