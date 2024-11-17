# import socket
# import time
#
# from ipv4 import IPPacket
# from layer4_socket import Layer4Socket
# from layer_3_socket import Layer3Socket
#
# host = '192.168.1.162'
# port = 5555
#
#
# # import psutil
# # addrs = psutil.net_if_addrs()
# # print(addrs.keys())
# # exit()
# s = Layer3Socket()
# s.connect("1.1.1.1")
# s.layer3send(b'HELLO')
# from l3socket_windows import L3SocketWindows
#
# s = L3SocketWindows()
# s.connect('192.168.1.1')
# s.layer3send(b"Hello this is some text to make it think thak isfdsio")
from layers.l2socket import Layer2Socket

# from pydivert import Packet, Direction, WinDivert
#
# from packets.ipv4 import IPPacket
# from packets.tcp import TCPPacket, TCPFlags
#
# with WinDivert("ip.SrcAddr == 192.168.1.162") as d:
#     # d.open()
#     # p=d.recv()
#
#     # print(p)
#     ipp = IPPacket(source="192.168.1.162", dest="2.2.2.2", payload=TCPPacket(src_port=1234, dest_port=5678, flags=[TCPFlags.SYN]).build())
#     p = Packet(ipp.build(), (9, 0), Direction.OUTBOUND)
#     print(p)
#     d.send(p)

s = Layer2Socket()

print(p.hex())
