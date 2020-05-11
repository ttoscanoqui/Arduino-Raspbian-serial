import time
import serial
import requests
import json

try:
  ser = serial.Serial('/dev/ttyS0')	#depending of you raspberry, you may use ttyACM# or ttyUSB#
  
  while True:
    ser.flush()
    line = ser.readline().strip()
    lista = line.decode().split(',')
    print(lista)
    
    #Write data to Thingsboard
    if len(lista) == 2:
        enviar = requests.get("https://api.thingspeak.com/update?api_key=XXXXXXXXXXXXXXXX&field1="+str(lista[0])+"&field2="+str(lista[1]))
        if enviar.status_code == requests.codes.ok:
            if enviar.text != '0':
                print("Datos enviados correctamente")
            else:
                print("Tiempo de espera insuficiente (>15seg)")
        else:
            print("Error en el request: ",enviar.status_code)
    else:
        print("La cadena recivida no contiene 2 elementos, sino:",len(lista),"elementos")

    #Read data from Thingsboard
    recibir = requests.get("https://api.thingspeak.com/channels/xxxxxxx/feeds.json")
    jsonString = json.dumps(recibir.json(),indent=2)
    print(jsonString)
    
    print("-------------------------------------------------")
    jsonString = json.dumps(recibir.json().get("feeds"),indent=2)
    print(jsonString)
    
    print("----Mostrar la info de los primeros 3 valores----")
    num = 3 if len(recibir.json().get("feeds"))>3 else len(recibir.json().get("feeds"))

    for i in range(num):
        print("*************************************************")
        jsonString = json.dumps(recibir.json().get("feeds")[i],indent=2)
        print(jsonString)
    
    print("-------Mostrar solo los primeros 3 valores-------")
    for i in range(num):
        print("*************************************************")
        print("Variable1:",recibir.json().get("feeds")[i].get("field1"))
        print("Variable2:",recibir.json().get("feeds")[i].get("field2"))

    print("----Mostrar la info de los ultimos 3 valores-----")
    recibir = requests.get("https://api.thingspeak.com/channels/xxxxxxx/feeds.json?results="+str(num))
    jsonString = json.dumps(recibir.json().get("feeds"),indent=2)
    print(jsonString)
    
    print("-------Mostrar solo los ultimos 3 valores-------")
    for i in range(num):
        print("*************************************************")
        print("Variable1:",recibir.json().get("feeds")[i].get("field1"))
        print("Variable2:",recibir.json().get("feeds")[i].get("field2"))
    
    time.sleep(15)
    
except KeyboardInterrupt: #close serial comunication when user force stop
  print ()
  ser.close()