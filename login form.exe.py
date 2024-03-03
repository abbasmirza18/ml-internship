#login form
from tkinter import *
from tkinter import messagebox
import subprocess

import tkinter
from PIL import Image,ImageTk

top=Tk()
#top.geometry("1366x768")
top.title("LOGIN FORM")
# Create a photoimage object of the image in the path
image1 = Image.open("login.jpg")
top.geometry("1366x768")

image1 = image1.resize((1366, 768))
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)



def valid():
    uid=t1.get()
    pwd=t2.get()
    if( uid=="python" and pwd=="bdps"):
        subprocess.run(["python", "bank form.py"])

       #exec(open("bank form.py").read())
       
    else:
        messagebox.showinfo("Conformation","Invalid User id/Password")
        t1.delete(0,15)
        t2.delete(0,15)
        t1.focus()


"""top.configure(bg="light blue")"""


l= Label(top,text="LOGIN FORM",font=("Engravers MT",25),fg="black",bg="white")
l.place(x=200+400+200,y=50+100)
l1 = Label(top,text="Enter User Id ",font=("Footlight MT Light",15),fg="black",bg="white")
l1.place(x=50+650,y=125+100+50)
l2 = Label(top,text="Enter Password ",font=("Footlight MT Light",15),fg="black",bg="white")
l2.place(x=50+650,y=175+100+100)
t1= Entry(top,width=30,bg="gainsboro")
t1.place(x=250+650,y=125+100+50+5)
t2= Entry(top,width=30,bg="gainsboro",show="*")
t2.place(x=250+650,y=125+100+150+5)
b1= Button(top,text="OK",width=15,bg="green",fg="white",font=("Footlight MT Light",13),command=valid)
b1.place(x=270+650,y=125+100+150+5+100)

b2= Button(top,text="CANCEL",width=15,bg="dark red",fg="white",font=("Footlight MT Light",13),command=top.destroy)
b2.place(x=70+650,y=125+100+150+5+100)

t1.focus()
top.mainloop()
