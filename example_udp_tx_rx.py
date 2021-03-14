import socket
import struct


# Set up socket
HOST = '192.168.178.22'  # Add the IP of this Device
PORT = 2200              # Use a free Portnumber

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket created')


# Error handling for Socket
try:
    s.bind((HOST, PORT))
    print('Waiting client...')
except socket.error:
    print('Bind failed')
    s.close()
    


# Communicate with Simulink
while True:
   
    data_get, add = s.recvfrom(2048)

    data_get = data_get
    
    # How many values were send? Devided by the Datatype you choosed in your Simulinkmodel
    numOfValues = len(data_get) / 4
    numOfValues = int(numOfValues)
        
    # converting Bytes "<" = little endian "f" =float (4byte)
    mess = struct.unpack('<' +'f' * numOfValues, data_get)
    
    print(HOST+", "+str(PORT)+": "+str(mess))

            
    # Send everything back

    s.sendto(data_get, add)

   



