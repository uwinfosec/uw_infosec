#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from scapy.utils import rdpcap

pkts = rdpcap("your_bittorrent_file_name")

#loop through each packet
#inspect it
# see if there's any pattern you can find
# recommend finding pattern in wireshark first, 
# and creating algorithm in python to detect it.

