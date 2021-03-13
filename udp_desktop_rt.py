import socket
import random
import struct
import time
import math

#Set up socket
HOST = '192.168.178.22'  #Server-IP
PORT = 2200

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
V_ist = 200

#Mit client sprechen
while True:
   
    data_get,add = s.recvfrom(2048)
    
    
    ist_values = struct.pack('<ff',RPM_ist,V_ist)
    
    data_get = data_get + ist_values
    
    #wie viele Werte kommen an? Haengt im Datentyp in Matlab ab
    numOfValues = len(data_get) / 4
    numOfValues = int(numOfValues)
        
    #bytes konvertieren <=little endian d=double (8byte)
    mess=struct.unpack('<' +'f' * numOfValues, data_get)
    
    print (HOST+", "+str(PORT)+": "+str(mess))
    
    if mess[1] == 1 and mess[3] == 2:
        if mess[4] > RPM_ist and mess[5] > V_ist:
            RPM_ist += 1
            V_ist += 1
        elif mess[4] < RPM_ist and mess[5] < V_ist:
            RPM_ist -= 1
            V_ist -= 1
        elif mess[4] > RPM_ist and mess[5] == V_ist:
            RPM_ist += 1
        elif mess[4] < RPM_ist and mess[5] == V_ist:
            RPM_ist -= 1
        elif mess[5] > V_ist and mess[4] == RPM_ist:
            V_ist += 1
        elif mess[5] < V_ist and mess[4] == RPM_ist:
            V_ist -= 1
        elif mess[4] > RPM_ist and mess[5] < V_ist:
            RPM_ist += 1
            V_ist -= 1
        elif mess[4] < RPM_ist and mess[5] > V_ist:
            RPM_ist -= 1
            V_ist += 1
            
    #Daten zurueck an Senden
    if mess[1] == 1:
        s.sendto(data_get,add)

   



