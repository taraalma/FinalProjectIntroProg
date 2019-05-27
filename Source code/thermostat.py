# array for each color of the gradient
gradientList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# colors for each gradient.
arrayColores = ['#E50000','#DD0008','#D60010','#CE0018','#C70020','#C00029','#B80031','#B10039','#A90041','#A2004A','#9B0052','#93005A','#8C0062','#84006A','#7D0073','#76007B','#6E0083','#67008B','#600094','#58009C','#5100A4','#4900AC','#4200B4','#3B00BD','#3300C5','#2C00CD','#2400D5','#1D00DE','#1600E6','#0E00EE','#0700F6','#0000FF','#FFFFFF']

# Gradient class for objects with different color.
class Gradient:
	
	IsObjectHidden = 0
	
	def __init__(self, canvas, xStartval, yStartval, xFinVal, yFinVal, x):
		
		self.xStartingValue  = xStartval
		self.yStartingValue  = yStartval
		self.xFinalValue 	 = xFinVal
		self.yFinalValue 	 = yFinVal
		self.GradientColor	 = x
		self.draw(canvas)
		
	def draw(self, canvas):
		global arrayColores
		
		gradientObjectColor = str(arrayColores[32 - self.GradientColor])
		self.canvas = canvas
		if (self.IsObjectHidden == 0):
			self.id = canvas.create_rectangle(self.xStartingValue, self.yStartingValue, self.xFinalValue, self.yFinalValue, width=5 , fill=gradientObjectColor,outline=gradientObjectColor)
		else:
			self.id = canvas.create_rectangle(self.xStartingValue, self.yStartingValue, self.xFinalValue, self.yFinalValue, width=5 , fill='#FFFFFF',outline='#FFFFFF')

class Gui():
	def __init__(self, tk):
		self.tk=tk
		self.entry = Entry(tk)
		stvar=StringVar()
		stvar.set("one")

		self.canvas=Canvas(tk, width=300, height=200, background='white')
		self.canvas.grid(row=0,column=1)

		frame = Frame(self.tk)
		frame.grid(row=0,column=0, sticky="n")

		self.option=OptionMenu(frame, stvar, "one", "two", "three")
		label1=Label(frame, text="Figure").grid(row=0,column=0, sticky="nw")
		label2=Label(frame, text="X").grid(row=1,column=0, sticky="w")
		label3=Label(frame, text="Y").grid(row=2,column=0, sticky="w")
		self.option.grid(row=0,column=1,sticky="nwe")
		entry = Entry(frame).grid(row = 1,column = 1,sticky = E+ W)
		entry1 = Entry(frame).grid(row = 2,column = 1, sticky = E)
		Button1=Button(frame,text="Draw").grid(row = 3,column = 1, sticky = "we")
		figure1=self.canvas.create_rectangle(80, 80, 120, 120, fill="blue")

		#Grid.columnconfigure(self.tk,1,weight=1, size=200)
