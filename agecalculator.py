#from PIL import Image, ImageTk # did not run when I chose the name for 'ImageTk' - use 'ImageTk'
import tkinter as windowOne # 'windowOne' is a created name
import datetime # need 'datetime' for calculating age

class Person:

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self): # useful to have for the command line
        return "{}:{}".format(self.name, self.birthdate)

    def getage(self):
        birthdate = self.birthdate # without .year output will return in days
        now = datetime.date.today() # without .year output will return in days
        age = ((now-birthdate)/365.25).days # 'age' is a timedelta object because I subtracted 2 date objects (i.e. now-birthdate). timedeltas have a .days function
        return age

def calculate(): # notice how this eventhandler is outside of class 'Person' so it is not limited to that scope
    yearC = int(yearEntry.get())
    monthC = int(monthEntry.get())
    dayC = int(dayEntry.get())
    subject = Person("This person", datetime.date(yearC, monthC, dayC))

    textWindow = windowOne.Text(master=window, height=25 , width=25, highlightcolor = "blue")
    textWindow.grid(column = 1, row = 6)

    sentence = "{} is {} years old".format(nameEntry.get(), subject.getage())
    textWindow.insert(windowOne.END, sentence)
    #print (subject.getAge())

window = windowOne.Tk()
window.title("Cold Creator Calculator") # creates a custom title in frame header
window.geometry("400x400") # consider using 'pack' so that the frame size adjusts to its contents

#photoPath = Image.open("/Users/Malik/desktop/cc_logo_white2.jpg") # store the image path within this vaiable by using Image.open
#photoPath.thumbnail((100,100), Image.ANTIALIAS) #
#photo = ImageTk.PhotoImage(photoPath) # create photo using the storage variable containing path (i.e. 'photoPath')
#photoLabel = windowOne.Label(image = photo) # photos can be stored in labels
#photoLabel.grid(column = 1, row = 0)

nameLabel = windowOne.Label(window, text = "Name")
nameLabel.grid(column = 0, row = 1)
nameEntry = windowOne.Entry(window)
nameEntry.grid(column = 1, row = 1)

yearLabel = windowOne.Label(window, text = "Year")
yearLabel.grid(column = 0, row = 2)
yearEntry = windowOne.Entry(window)
yearEntry.grid(column = 1, row = 2)

monthLabel = windowOne.Label(window, text = "Month")
monthLabel.grid(column = 0, row = 3)
monthEntry = windowOne.Entry(window)
monthEntry.grid(column = 1, row = 3)

dayLabel = windowOne.Label(window, text = "Day")
dayLabel.grid(column = 0, row = 4)
dayEntry = windowOne.Entry(window)
dayEntry.grid(column = 1, row = 4)

calculateButton = windowOne.Button(text = "Calculate Age", command = calculate) # .Button(text, command) is an alternative to .bind(text, event) e.g. line 50
calculateButton.grid(column = 1, row = 5)
#calculateButton.bind("<Button-1>", calculate)

window.mainloop()
#malik = Person("Malik", datetime.date(1989, 5, 31))
#malik.getAge()


