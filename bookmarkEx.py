import tkinter as windowOne # if any problems import as 'tk' instead
import webbrowser

URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Banana-Single.jpg/1200px-Banana-Single.jpg"

def add1(event):
	print ("1 Banana added to the shelf")

def harvest(event):
	print ("Harvest Time!!")

def seeBanana(event):
	webbrowser.open_new_tab(URL)

window = windowOne.Tk() # 'window' constructor
window.geometry("500x500") # changes window size (width x height)

bananaLabel = windowOne.Label(text = "banana")
bananaLabel.grid(column = 0, row = 0)

bananaButton = windowOne.Button(window, text = "See")
bananaButton.grid(column = 0, row = 1)

add1Button = windowOne.Button(window, text = "ADD 1") # the name of the frame is the 1st argu. i.e. 'window'
add1Button.grid(column = 0, row = 2)

harvestButton = windowOne.Button(window, text = "Harvest")
harvestButton.grid(column = 0, row = 3)

add1Button.bind("<Button-1>", add1) # binds the 'add1' event handler to the left click (button-1) and 'add1Button'
harvestButton.bind("<Button-1>", harvest)
bananaButton.bind("<Button-1>", seeBanana)

window.mainloop()

