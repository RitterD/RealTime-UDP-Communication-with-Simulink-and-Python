<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Introduction](#introduction)

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

