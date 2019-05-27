from tkinter import *
import random
import time
from thermostat import *

oddNon = 0
GradientList = []
xWidth = 40

# Start program
tk = Tk()
tk.title("Monitor for sensor stuff")

canvas = Canvas(tk, width = (xWidth + 5), height = 125, bd = 0, highlightthickness = 0, bg = '#FFFFFF')
canvas.grid(row=0,column=1)

#canvas.pack()
tk.update()


entry = Entry(tk)
stvar=StringVar()
stvar.set("one")
frame = Frame(tk)
frame.grid(row=0,column=0, sticky="n")

option=OptionMenu(frame, stvar, "one", "two", "three")
label1=Label(frame, text="Figure").grid(row=0,column=0, sticky="nw")
label2=Label(frame, text="X").grid(row=1,column=0, sticky="w")
label3=Label(frame, text="Y").grid(row=2,column=0, sticky="w")
labelGradient = Label( frame, text="Temp: ", font ="Helvetica", anchor= SW,bg='#FFFFFF').grid(row=3,column=0, sticky="w")

option.grid(row=0,column=1,sticky="nwe")
entry = Entry(frame).grid(row = 1,column = 1,sticky = E+ W)
entry1 = Entry(frame).grid(row = 2,column = 1, sticky = E)
Button1=Button(frame,text="Draw").grid(row = 3,column = 1, sticky = "we")
figure1=canvas.create_rectangle(80, 80, 120, 120, fill="blue")



# Initialize gradients in a list
# the variable xWidth is used to determine the width of each gradient.

GradientList.append(Gradient(canvas,0,0,xWidth,4,31))
GradientList.append(Gradient(canvas,0,4,xWidth,8,30))
GradientList.append(Gradient(canvas,0,8,xWidth,12,29))
GradientList.append(Gradient(canvas,0,12,xWidth,16,28))
GradientList.append(Gradient(canvas,0,16,xWidth,20,27))
GradientList.append(Gradient(canvas,0,20,xWidth,24,26))
GradientList.append(Gradient(canvas,0,24,xWidth,28,25))
GradientList.append(Gradient(canvas,0,28,xWidth,32,24))
GradientList.append(Gradient(canvas,0,32,xWidth,36,23))
GradientList.append(Gradient(canvas,0,36,xWidth,40,22))
GradientList.append(Gradient(canvas,0,40,xWidth,44,21))
GradientList.append(Gradient(canvas,0,44,xWidth,48,20))
GradientList.append(Gradient(canvas,0,48,xWidth,52,19))
GradientList.append(Gradient(canvas,0,52,xWidth,56,18))
GradientList.append(Gradient(canvas,0,56,xWidth,60,17))
GradientList.append(Gradient(canvas,0,60,xWidth,64,16))
GradientList.append(Gradient(canvas,0,64,xWidth,68,15))
GradientList.append(Gradient(canvas,0,68,xWidth,72,14))
GradientList.append(Gradient(canvas,0,72,xWidth,76,13))
GradientList.append(Gradient(canvas,0,76,xWidth,80,12))
GradientList.append(Gradient(canvas,0,80,xWidth,84,11))
GradientList.append(Gradient(canvas,0,84,xWidth,88,10))
GradientList.append(Gradient(canvas,0,88,xWidth,92,9))
GradientList.append(Gradient(canvas,0,92,xWidth,96,8))
GradientList.append(Gradient(canvas,0,96,xWidth,100,7))
GradientList.append(Gradient(canvas,0,100,xWidth,104,6))
GradientList.append(Gradient(canvas,0,104,xWidth,108,5))
GradientList.append(Gradient(canvas,0,108,xWidth,112,4))
GradientList.append(Gradient(canvas,0,112,xWidth,116,3))
GradientList.append(Gradient(canvas,0,116,xWidth,120,2))
GradientList.append(Gradient(canvas,0,120,xWidth,124,1))
GradientList.append(Gradient(canvas,0,124,xWidth,128,0))


#labelGradient.pack()

while 1:

	if ( oddNon == 1):
		for y in range (0,32):
			GradientList[y].IsObjectHidden = 1
			GradientList[y].draw(canvas)
		oddNon = 0

	else:
		for y in range (0,32):
			GradientList[y].IsObjectHidden = 0
			GradientList[y].draw(canvas)
		oddNon = 1
	
	tk.update_idletasks()
	tk.update()
	time.sleep(0.68)
