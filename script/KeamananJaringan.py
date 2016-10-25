#!/bin/python

"""
class NITA network 
"""
from scapy.all import ARP,Ether,sendp


class KeamananJaringan(object):
	def sendArp(self,mac_rec,ip_rec,ip_target):	
		paket = Ether()/ARP(op="who-has",hwsrc=mac_rec,psrc=ip_rec,pdst=ip_target)
 		sendp(paket)