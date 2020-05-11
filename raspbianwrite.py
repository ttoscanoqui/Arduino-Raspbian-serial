##Raspberry Pi : Emissor
##Before create code, install the 'python-serial' library with the command
##sudo apt-get install python-serial

##Code:

import serial
arduino = serial.Serial('/dev/ttyACM0',9600)
print("starting")
while(True):
	comando = raw_input('introduce un comando: ')
	arduino.write(comando)
	if comando == 'H':
		print('led encendidio')
	elif comando == 'L':
		print("led apagado")
arduino.close()
