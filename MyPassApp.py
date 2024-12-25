import tkinter as tk
import random
from tkinter import messagebox

def random_password():
    a = ['a', 'b', 'c', 'd', 'e']
    b = ['1', '2', '3', '4', '5']
    c = ['/', '@', '.', ',', '$']
    listi = a + b + c
    random.shuffle(listi)
    password = ""
    for i in range(8):
        password = password + listi[i]
    entry3.delete(0,tk.END)
    entry3.insert(0,password)

def find():
    with open("data.txt","r") as d:
        data = d.readlines()
        for podatok in data:
            lista_podatok = podatok.split("|")
            if entry1.get().strip() == lista_podatok[0].strip():
                messagebox.showinfo("Password and email", f"Email: {lista_podatok[1]}\nPassword: {lista_podatok[2]}")

def add():
    text_web = entry1.get()
    text_email = entry2.get()
    text_pas = entry3.get()
    print("a")
    if text_email and text_web and text_pas:
        text = f"{text_web} | {text_email} | {text_pas}\n"
        entry1.delete(0,tk.END)
        entry2.delete(0,tk.END)
        entry3.delete(0,tk.END)
        with open("data.txt", 'a') as data:
            data.write(text)
    else:
        messagebox.showinfo("Input Error", "Popolni gi site polinja pred da zacuvas")

screen=tk.Tk()
screen.geometry("500x500")

screen.columnconfigure(0, weight=1)
screen.columnconfigure(1, weight=1)
screen.columnconfigure(2, weight=1)

canvas = tk.Canvas()

img = tk.PhotoImage(file="image.png")
canvas.config(width=200,height=200)
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)


label1=tk.Label(text="Website: ")
label1.grid(row=1,column=0,)

entry1=tk.Entry()
entry1.grid(row=1,column=1)

label2=tk.Label(text="Email/Username: ")
label2.grid(row=2,column=0)

entry2=tk.Entry()
entry2.grid(row=2,column=1)

label3=tk.Label(text="Password: ")
label3.grid(row=3,column=0)

entry3=tk.Entry()
entry3.grid(row=3,column=1)

button=tk.Button(text="Add",height=0, width=16, command=add)
button.grid(row=4,column=1)

button1=tk.Button(text="Generate Password",width=16, command=random_password)
button1.grid (row=3,column=2)

button2=tk.Button(text="Find",width=16,command=find)
button2.grid (row=2,column=2)




screen.mainloop()
