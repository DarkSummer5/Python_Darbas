from tkinter import *
import numpy as np
import sys
import os
import random
import time
window = Tk()
lbl=Label(window, text=" Žaidimai", fg='black',bg='#FFE4C4', font=("Helvetica", 20))
lbl.place(x=200, y=30)
window.geometry('500x500')
window.configure(bg='#FFE4C4')
def run1():
    os.system('sanke.py')
btn1 = Button(window, text = 'Gyvatėlė   ', bd='8',
                                command = run1)
btn1.place(x=350, y=100)
def run5():
        os.system('snake2.py')
btn8 = Button(window, text ='Gyvatėlė 2', bd='8',
                              command = run5)
btn8.place(x=350, y=135)
def run2():
        os.system('tic_tac_toe.py')
btn2 = Button(window, text = 'Tic     Tac      Toe       ', bd = '7',
                              command = run2)
btn2.place(x=80, y=100) 
def run3():
        os.system('brick_breaker.py')
btn3 = Button(window, text =" 'Brick Breaker' ", bd='8',
                                command = run3)
btn3.place(x=80, y=280)

def run4():
    os.system('2048.py')
btn4 = Button(window, text="2", bd='8', bg='#eee4da',
                                command = run4)
btn4.place(x=350, y=280)

btn5 = Button(window, text="0", bd='8', bg='#f59563',
                                command = run4)
btn5.place(x=380, y=280)
btn6 = Button(window, text="4", bd='8', bg='#ede0c8',
                                command = run4)
btn6.place(x=350, y=316)

btn7 = Button(window, text="8", bd='8', bg='#f2b179',
                                command = run4)
btn7.place(x=380, y=316)

def isjungimas():
        window.destroy()
isjungti = Button( text='Isjungti', width=25, command=isjungimas)
isjungti.place(x=170, y=450)
    
window.mainloop()