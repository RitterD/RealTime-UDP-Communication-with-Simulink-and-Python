<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Introduction](#introduction)
- [Getting started](#getting-started)
  - [Simulink](#simulink)
  - [RaspberryPi](#raspberrypi)
- [Set up your Simulink](#set-up-your-simulink)
  - [Sequence Number](#sequence-number)
  - [Run your Model](#run-your-model)
- [Python script for sending/receiving data](#python-script-for-sendingreceiving-data)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Introduction
This project is used to set up a real time communication between a Simulinkmodel and a RaspberryPi using UDP as transport protocol.
<b>Parts in the Simulinkmodel are still in German... As soon as I have the time I will add a full English version as well</b>

# Getting started
## Simulink
First of all you need to install the Matlab [Desktop Real-Time-Toolbox](https://mathworks.com/products/simulink-desktop-real-time.html). It provides a RT-Kernel for your Windows/MacOS and converts your Simulinkmodel into C-Code.

## RaspberryPi
Set up the RaspberryPi is pretty easy. If you want to send data over one IP only you can connect the computer and the RaspberryPi directly with an ethernet cabel or even more easy you can use WIFI. In my case I want to send data over two IPs. I used the standard ethernet port of the Raspberry and added an USB to ethernet adapter. Now, to connect computer and Raspberry use a HUB/Switch.

<p align="center">
    <img alt="Network" title="Network" src="https://github.com/RitterD/RealTime-UDP-Communication-with-Simulink-and-Python/blob/main/img/Network.png">
  </a>
</p>

# Set up Simulink
To send and receive data over TCP/UDP, choose the "Packet Output"/"Packet Input" blocks from the Destkop RealTime Toolbox. Open the block and "Install new board" select "standard devices" and then "UDP Protocol". Insert the IP-address of your RaspberryPi and the portnumber. I recommend a high portnumber (4 digits at least).
In the Input/Output section you have to adjust the packet sizes for incoming and outgoing bytestrings. For instance you send a sinwave with a datatype double (8byte) and an integer number (1byte) the Output packet size is 9Byte and the Outpacket field data types looks like: {'1double', '1int8} and two input/output ports will be created. 
<b>Attention: If you use constant blocks adjust them to the sample time of your send/receive blocks.</b>

## Sequence Number
The Sequence Number is the key in this realtime concept. With the sequence number you are upgrading your UDP-Protocol and eliminate all the disadvantages without giving up the advantages e.g. transmission speed and multicast.
For instance, the master sends a number which will be incremented with every msg and the slave sends this sequence number back you are able to check: 
<ol>
  <li>Is there a connection between master and slave</li>
  <li>Is there any package loss</li>
  <li>Did the slave receive the packages in the right order</li>
  <b><li>Is the real time condition still fulfilled</li></b>
</ol>

<p align="center">
    <img alt="SeqNr" title="SeqNr" src="https://github.com/RitterD/RealTime-UDP-Communication-with-Simulink-and-Python/blob/main/img/SequenceNumber.png">
  </a>
</p>

## Run the Model
Now you have to run your Simulinkmodel in <b>external mode</b>. For that, go to "APPS" and select "Desktop Real-Time". There you can run your model in Real Time.

# Python script for sending/receiving data
For this low level networking I used the [socket lib](https://docs.python.org/3/library/socket.html) and the [struct lib](https://docs.python.org/3/library/struct.html) for decoding the byte strings. The "example_udp_tx_rx.py" is an super easy example which receives data from the Simulinkmodel, prints it out and simply sends everything back to the master. This example you can use to understand how the communication works and if you set up everything correctly in Simulink. The "udp_desktop_rt" shows you how to add extra data from the slave side. In my project I used a second script to send/receive data over the second IP. It was convenient for finding errors and testing my model.
Just run the scripts in your command window. Once they are running you dont have to start them again. It works like a server client. The script waits for new data to send it back to the IP where the message came from. But remember, als long as the script is running the port you have given for the communication is blocked. 
