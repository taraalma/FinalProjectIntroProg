# Final project. Tkinter application.

import time
from tkinter import *
from random import *

# gradient for temperature
arrayColores = ['#E50700','#D6060C','#C80619','#BA0526','#AB0533','#9D0440','#8F044D','#80035A','#720367','#640274','#550281','#47018E','#39019B','#2A00A8','#1C00B5','#0E00C2']

def createAWindow():
	global arrayColores
	
	window = Tk()
	window.geometry('1000x600+10+10')
	canvas = Canvas(window, width=900, height=500)
	canvas.pack()
	
	for x in range (0,16):
		# modify only the xStartval to indicate where it shoul start
		xStartval = 90
		# modify the rectangleHeight value to indicate the height of the gradient
		rectangleHeight = 10
		yStartval = rectangleHeight + ( 10 * x )
		# modify the rectangleWidth value to indicate the width of the rectangle 
		rectangleWidth = 70
		xFinVal = xStartval + 70
		yFinVal = 10 + ( 10 * (1 + x) )
		colorito = str(arrayColores[x])
		canvas.create_rectangle(xStartval, yStartval, xFinVal, yFinVal, width=5 , fill=colorito,outline=colorito)

	window.title('generic tkinter window')
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


