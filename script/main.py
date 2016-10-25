#!nita/bin/python

import KeamananJaringan
Keamanan = kj.Keamanan()

while 1:
       Keamanan.sendArp('00:19:e3:d9:3f:6f','192.168.1.1','192.168.1.37')