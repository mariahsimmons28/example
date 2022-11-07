from tkinter import * # import tkinter module 
root = Tk() #tkinter interface 

root.geometry('500x500')
#creating label 
#.place - tells object where to go on GUI 
myLabel = Label(root, text = ' This is a Python GUI!').place(x = 150, y =150)
#adds widgets(label) to window 
#myLabel.pack() 

button = Button( root,
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()




root.mainloop()# tells Python to run the Tkinter event loop 