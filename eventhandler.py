import tkinter as windowOne # if any problems import as 'tk' instead
#from tkinter import ttk - this line imports ttk for labels

def add1(event):
	print ("1 Banana added to the shelf")

def harvest(event):
	print ("Harvest Time!!")

window = windowOne.Tk() # 'window' constructor
window.geometry("500x500") # changes window size (width x height)

bananaLabel = windowOne.Label(text = "banana")
bananaLabel.grid(column = 0, row = 0)

add1Button = windowOne.Button(window, text = "ADD 1") # the name of the frame is the 1st argu. i.e. 'window'
add1Button.grid(column = 0, row = 1)

harvestButton = windowOne.Button(window, text = "Harvest")
harvestButton.grid(column = 0, row = 2)

add1Button.bind("<Button-1>", add1) # binds the 'add1' event handler to the left click (button-1) and 'add1Button'
harvestButton.bind("<Button-1>", harvest) 

window.mainloop()

