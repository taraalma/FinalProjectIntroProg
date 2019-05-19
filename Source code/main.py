# Final project. Tkinter application.

# import modules
import time
import threading
from tkinter import *
from random import *
from thermostat import *

def createAWindow():
	global arrayColores
	global gradientList
	global numberOfGradients
	
	# this creates the main window.
	window = Tk()
	window.geometry('1000x600+10+10')
	canvas = Canvas(window, width=900, height=500)
	
	createButton(150,120)
	
	labelTimer = uglyLabel(window)
	
	canvas.pack()
	window.title('generic tkinter window')
	
	# This draws the thermometer. the range indicates how many gradients will be drawn.
	for x in range (0,numberOfGradients):
		# modify only the xStartval to indicate where it shoul start
		xStartval = 30
		# modify the rectangleHeight value to indicate the height of the gradient
		rectangleHeight = 4
		yStartval = 350 - ( rectangleHeight * x )
		# modify the rectangleWidth value to indicate the width of the rectangle 
		rectangleWidth = 70
		xFinVal = xStartval + 70
		yFinVal = 350 - ( rectangleHeight * (1 + x) )
		colorito = str(arrayColores[31 - x])
		# this initializes each gradient
		gradientList[x] = canvas.create_rectangle(xStartval, yStartval, xFinVal, yFinVal, width=5 , fill=colorito,outline=colorito)
	window.mainloop()

# this creates a button 
def createButton(xPos,yPos):
	mbutton = Button(text='Button Example',state=DISABLED).place(x=xPos,y=yPos)

# this creates an ugly string with text
class uglyLabel:
	def __init__(self,parent):
		self.seconds = 0
		self.label = Label(parent, text="0 s", font="Arial 30", width=10,fg='#00d7f3',bg='#ffffff' )
		#self.label = Label(parent, text="0 s",font=('bold'),fg='#00d7f3',bg='#ffffff').place(x=xPos,y=yPos)
		self.label.pack()
		self.label.after(1000, self.refreshLabel)
		
	def refreshLabel(self):
		self.seconds += 1
		self.label.configure(text="%i s" % self.seconds)
		self.label.after(1000, self.refreshLabel)

Thread_GUI = threading.Thread(target = createAWindow)

Thread_GUI.start()

# this initializes the main window and the whole GUI.

#time.sleep(60)
