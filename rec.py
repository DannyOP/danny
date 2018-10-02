#!/usr/bin/env python

import socket
import binascii
import struct

def main():

    MCAST_GRP = '224.0.0.1'
    MCAST_PORT = 10000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((MCAST_GRP, MCAST_PORT))
    # mreq = struct.pack("4s", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        print(sock.recvfrom(1024))

if __name__ == '__main__':
  main()
