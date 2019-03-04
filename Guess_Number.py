'''
Created on Mar 1, 2019

@author: s271486
'''

from tkinter import *

root = Tk()

Label1 = Label(root, text="Guess a number between 1 and 10:")
Label1.pack()

TextBox = Entry(root)
TextBox.pack()

def calculate():
    userinput = TextBox.get()
    guess = int(userinput)
    correct_number = 3
    Answer = Label(root, text="Wow you're a genius")
    if guess == correct_number:
        Answer.pack()
    TooHigh = Label(root, text="You're answer is too high")
    if guess > correct_number:
        TooHigh.pack()
    TooLow = Label(root, text="You're answer is too Low")
    if guess < correct_number:
        TooLow.pack()
        
ClickMe = Button(root, text="ClickMe", command=calculate)

ClickMe.pack()        

root.mainloop()
        
        

    