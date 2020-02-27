# PortScanner

Port scanner in Python. It checks which ports(number and service) are open. Interface developed in PySimpleGUI.

## Requirements

```
Install Python
pip install socket
pip install scapy
pip install PySimpleGUI
```

## How to run

On terminal:

```
sudo su
python port_scanner.py
```

Run as root is necessary because of scapy library.

## How to use

### Check ports at a Host

![alt text](https://github.com/gabriellm1/PortScanner/blob/master/images/host_print.png)

1. Select 'Host'
2. Input IP
3. Input range of ports
4. Select TCP or UDP
5. Click 'Iniciar'

### Check ports at a Network

![alt text](https://github.com/gabriellm1/PortScanner/blob/master/images/rede_print.png)

1. Select 'Rede'
2. Input IP range (format example -> '192.168.1.1-192.168.1.100')
3. Input range of ports
4. Select TCP or UDP
5. Click 'Iniciar'
