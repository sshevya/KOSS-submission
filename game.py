import pygame
import Tkinter
import sys
import random

cpu_random=random.randint(1,3)

def rock():
   if cpu_random==1:
       print("tie")
   elif cpu_random==2:
       print("you lose")
   elif cpu_random==3:
       print("you win")
def paper():
   if cpu_random==1:
       print("you win")
   elif cpu_random==2:
       print("tie")
   elif cpu_random==3:
       print("you lose")
def scissor():
   if cpu_random==1:
       print("you lose")
   elif cpu_random==2:
       print("you win")
   elif cpu_random==3:
       print("tie")

root=Tkinter.Tk()
topFrame=Tkinter.Frame(root)
topFrame.pack()
root.title("game")
root.geometry("200x160")

#bottomFrame=Tkinter.Frame(root)'
#bottomFrame.pack()
button1=Tkinter.Button(topFrame,width=10,text="rock",fg="white",bg="red",command=rock)
button2=Tkinter.Button(topFrame,width=10,text="paper",fg="white",bg="red",command =paper)
button3=Tkinter.Button(topFrame,width=10,text="scissor",fg="white",bg="red",command=scissor)
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)         
root.mainloop()
