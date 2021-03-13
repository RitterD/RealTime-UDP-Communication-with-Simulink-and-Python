import socket
import random
import struct
import time
import math

#Set up socket
HOST = '192.168.178.54'  #Server-IP
PORT = 5400

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ('Socket created')

#Verbingungsaufbau: UDP braucht nur bind
#Error handling for Socket
try:
    s.bind((HOST, PORT))
    print ('Warte auf client...')
except socket.error:
    print ('Bind failed')
    s.close()
    

RPM_ist = 100
Amp_ist = 200

#Mit client sprechen
while True:
   
    data_get,add = s.recvfrom(2048)
    
    
    ist_values = struct.pack('<ff',RPM_ist,Amp_ist)
    
    data_get = data_get + ist_values
    
    #wie viele Werte kommen an? Haengt im Datentyp in Matlab ab
    numOfValues = len(data_get) / 4
    numOfValues = int(numOfValues)
        
    #bytes konvertieren <=little endian d=double (8byte)
    data=struct.unpack('<' +'f' * numOfValues, data_get)
    
    print (HOST+", "+str(PORT)+": "+str(data))
    
    if data[1] == 1 and data[3] == 2:
        if data[4] > RPM_ist and data[5] > Amp_ist:
            RPM_ist += 1
            Amp_ist += 1
        elif data[4] < RPM_ist and data[5] < Amp_ist:
            RPM_ist -= 1
            Amp_ist -= 1
        elif data[4] > RPM_ist and data[5] == Amp_ist:
            RPM_ist += 1
        elif data[4] < RPM_ist and data[5] == Amp_ist:
            RPM_ist -= 1
        elif data[5] > Amp_ist and data[4] == RPM_ist:
            Amp_ist += 1
        elif data[5] < Amp_ist and data[4] == RPM_ist:
            Amp_ist -= 1
        elif data[4] > RPM_ist and data[5] < Amp_ist:
            RPM_ist += 1
            Amp_ist -= 1
        elif data[4] < RPM_ist and data[5] > Amp_ist:
            RPM_ist -= 1
            Amp_ist += 1
        
    #Daten zurueck an Senden
    if data[1] == 1:
        s.sendto(data_get,add)




