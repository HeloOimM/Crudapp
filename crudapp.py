import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import csv
import re
import os
from pathlib import Path
crud = tk.Tk()
crud.geometry("1000x1000")
crud.title("Helo File Maker!")
def label(texts, xs, ys, heights, widths):
    tk.Label(crud, text=texts, font=('Noto Serif JP', 10, 'bold')).place(x=xs, y=ys, height = heights, width = widths)
    
def ent(data, xs, ys, heights, widths):
    tk.Entry(crud, textvariable = data,font=('Noto Serif JP', 10, 'bold')).place(x=xs, y=ys, height = heights, width = widths)
    
def but(texts, command, xs, ys, heights, widths):
    tk.Button(crud, text = texts,font=('Noto Serif JP', 10, 'bold'), command = command).place(x=xs, y=ys, height = heights, width = widths)
    
def big(xs, ys, heights, widths):
    mi = tk.Text(crud,font=('Noto Serif JP', 10, 'bold'),wrap="word")
    mi.place(x=xs, y=ys, height=heights, width=widths)
    return mi
    
filename = tk.StringVar()
search = tk.StringVar()
ph = []
def make(name,data,display):
    if (name == '' or data == ''):
        messagebox.showinfo("Nope :P",f"U can't leave it js blank >:(")
        display.delete('1.0', tk.END)
        display.insert('1.0',f"U can't leave it js blank >:(")
    else:  
        try:
            with open(f"{name}.txt", mode='w') as f:
                f.write(str(data))
            messagebox.showinfo("Yay!",f"Thing {name} made...")
            display.delete('1.0', tk.END)
            display.insert('1.0',f'Thing {name} made...')
        except Exception as e:
            messagebox.showinfo("???",f"Thing {name} is not behaving well!")
            display.delete('1.0', tk.END)
            display.insert('1.0',f'Thing {name} is weird :>')
        
def add(name,data,display,):
    if (name == '' or data == ''):
            messagebox.showinfo("Nope :P",f"U can't leave it js blank >:(")
            display.delete('1.0', tk.END)
            display.insert('1.0',f"U can't leave it js blank >:(")
    elif not Path(f"{name}.txt").exists():
            messagebox.showinfo("ERRoR",f"Searching for a {name} that doesn't exist")
            display.delete('1.0', tk.END)
            display.insert('1.0',f"Unfortunate.")
    else:
        try:
            with open(f"{name}.txt", mode='a', newline = '') as f:
                f.write(f"{str(data)}")
            with open(f"{name}.txt", mode='r') as f:
                display.delete('1.0', tk.END)
                messagebox.showinfo("Woah!",f"Thing {data} got added :o")
                t = f.readlines()
                display.insert('1.0',''.join(t))
        except Exception as e:
            messagebox.showinfo("???",f"Thing {name} violates rules :/")
            display.delete('1.0', tk.END)
            display.insert('1.0',f'Thing {name} violates rules :/')
            
def read(name,display,shows):
    if not Path(f"{name}.txt").exists():
        messagebox.showinfo("ERRoR",f"同じ繰り返し\nいつも回っている")
        display.delete('1.0', tk.END)
        display.insert('1.0',f"What... js happened???")
    else:
        try:
            with open(f"{name}.txt", mode='r') as f:
                display.delete('1.0', tk.END)
                shows = f.readlines()
                messagebox.showinfo("Reading...",f"Js press the button...")
                display.insert('1.0',''.join(shows))
                
        except Exception as e:
            messagebox.showinfo("???",f"Tough Luck?")
            display.delete('1.0', tk.END)
            display.insert('1.0',f'Replenish your day with an apple a day! ^w^')
            
def find(name,find,replace,display):
    if (find == '' or replace == ''):
        messagebox.showinfo("Nope :P",f"U can't leave it js blank >:(")
        display.delete('1.0', tk.END)
        display.insert('1.0',f"no...")
    elif not Path(f"{name}.txt").exists():
            messagebox.showinfo("ERRoR",f"Ur thing is null...")
            display.delete('1.0', tk.END)
            display.insert('1.0',f"Try again! :|")
    else:
        try: 
            with open(f"{name}.txt", mode='r') as f:
                t = f.read()
            if find in t:
                with open(f"{name}.txt", mode='w') as f:
                        stuff = t.replace(find,replace)
                        f.write(stuff)
                with open(f"{name}.txt", mode='r') as f:
                        display.delete('1.0', tk.END)
                        t = f.readlines()
                        messagebox.showinfo("Success",f"Yippee..")
                        display.insert('1.0',''.join(t))
            else:
                    messagebox.showinfo("Not(Exist)",f"Woops...")
                    display.delete('1.0', tk.END)
                    display.insert('1.0',"It's ok..?")
        except Exception as e:
            messagebox.showinfo("???",f"Error ^w^")
            display.delete('1.0', tk.END)
            display.insert('1.0',f'Thing creates an Error')
            
def delete(name, display):
    if (name == '' or data == ''):
        messagebox.showinfo("Nope :P",f"U can't leave it js blank >:(")
        display.delete('1.0', tk.END)
        display.insert('1.0',f"U can't leave it js blank >:(")
    elif not Path(f"{name}.txt").exists():
        messagebox.showinfo("ERRoR",f"Does not exist")
        display.delete('1.0', tk.END)
        display.insert('1.0',f"Hello... I'm")
    else:
        try:
            os.remove(f"{name}.txt")
            messagebox.showinfo("Gone!", "Poof :(")   
            display.delete('1.0', tk.END)
            display.insert('1.0',f'Thing {name} deleted...')
        except Exception as e:
            messagebox.showinfo("Nope :P",f"Nothing")
            display.delete('1.0', tk.END)
            display.insert('1.0',f"How did we get here?")
label("Name:", 10, 0,30,50)
ent(filename,60,0,30,300)

label("Stuff:", 10, 50,30,50)
data = big(15, 75, 300, 350)


label("Show:", 550, 50,30,50)
display = big(550, 75, 300, 350)

label("Find:", 10, 400,30,50)
search = big(10,425,50,350)

label("Sub:", 550, 400,30,50)
replace = big(550,425,50,350)

but("Make",lambda: make(filename.get(), data.get("1.0","end-1c"),display), 400,75,50,100)
but("+",lambda: add(filename.get(), data.get("1.0","end-1c"),display), 400,150,50,100)
but("See",lambda: read(filename.get(),display,ph), 400,225,50,100)
but("Change",lambda: find(filename.get(),search.get("1.0","end-1c"),replace.get("1.0","end-1c"),display), 400,430,50,100)
but(":/",lambda: delete(filename.get(),display), 10,500,50,100)

crud.mainloop()