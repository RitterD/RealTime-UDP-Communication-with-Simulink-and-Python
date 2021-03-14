<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Introduction](#introduction)
- [Getting started](#getting-started)
  - [Simulink](#simulink)
  - [RaspberryPi](#raspberrypi)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Introduction
This project is used to set up a real time communication between a Simulinkmodel and a RaspberryPi using UDP as transport protocol.

# Getting started
## Simulink
First of all you need to install the Matlab [Desktop Real-Time-Toolbox](https://mathworks.com/products/simulink-desktop-real-time.html). It provides you a RT-Kernal in your Windows/MacOS and converts your Matlabmodel into C-Code.

## RaspberryPi
To set up the RaspberryPi is pretty easy. If you want to send data over one IP only you can connect the computer and the RaspberryPi directly with an ethernet cabel or even more easy you can use WIFI. To be honist, in never used WIFI so I realy dont know how it works out. In my case I want to send data over two IPs. I used the standard ethernet port of the Raspberry and added an USB to ethernet adapter. Now, to connect computer and Raspberry use a HUB/Switch.

<p align="center">
  <a href="https://blackforestformula.hs-offenburg.de/">
    <img alt="Network" title="Network" src="https://github.com/RitterD/RealTime-UDP-Communication-with-Simulink-and-Python/blob/main/img/Network.png">
  </a>
</p>

# Set up your Simulink
To send and receive data over TCP/UDP, choose the "Packet Output"/"Packet Input" blocks from the Destkop RealTime Toolbox. Open the block and "Install new board" select "standard devices" and then "UDP Protocol". Insert the IP-addres of your RaspberryPi and the portnumber. I recommend a high portnumber (4 digits at least).
In the Input/Output section you have to adjust the packet sizes for incoming and outgoing bytestrings. For instance you send a sinwave with a datatype double (8byte) and an intege number (1byte) the Output packet size is 9Byte and the Outpacket field data types is: {'1double', '1int8} and two input/output ports will be created. 
<b>Attention: If you are choosing constant blocks adjust them to the sample time of your send/receive blocks.</b>
