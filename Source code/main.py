# Final project. Tkinter application.

import time
from tkinter import *
from random import *

# gradient for temperature
arrayColores = ['#E50000','#DD0008','#D60010','#CE0018','#C70020','#C00029','#B80031','#B10039','#A90041','#A2004A','#9B0052','#93005A','#8C0062','#84006A','#7D0073','#76007B','#6E0083','#67008B','#600094','#58009C','#5100A4','#4900AC','#4200B4','#3B00BD','#3300C5','#2C00CD','#2400D5','#1D00DE','#1600E6','#0E00EE','#0700F6','#0000FF']

gradientList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def createAWindow():
	global arrayColores
	global gradientList
	
	window = Tk()
	window.geometry('1000x600+10+10')
	canvas = Canvas(window, width=900, height=500)
	canvas.pack()
	window.title('generic tkinter window')
	
	# This draws the thermometer 
	
	for x in range (0,32):
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
		
		gradientList[x] = canvas.create_rectangle(xStartval, yStartval, xFinVal, yFinVal, width=5 , fill=colorito,outline=colorito)
		

	createButton(150,120)
	createUglyText(200,200)
	window.mainloop()
	

def createButton(xPos,yPos):
	mbutton = Button(text='Button Example',state=DISABLED).place(x=xPos,y=yPos)

def createUglyText(xPos,yPos):
	textToInput = 'Text Example'
	mLable = Label(text=textToInput,font=('bold'),fg='#00d7f3',bg='#ffffff').place(x=xPos,y=yPos)


createAWindow()


#time.sleep(60)


