import serial
ser = serial.Serial("COM16", 57600)

while True:
	raw = ser.readline()
	cc  = str(raw)
	char = (cc[2:][:-5])
	print ( char )
	#print ( raw )
