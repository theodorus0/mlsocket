import socket

from iptools import local_ip
from layers.l2socket import Layer2Socket
from packets.ipv4 import IPPacket


class Layer3Socket(Layer2Socket):
    _socket: socket.socket
    local_addr: str

    def __init__(self):
        super().__init__()
        self.local_addr = local_ip

    def sendto3(self, payload: bytes, destination: str):
        """Send Layer 3 (IP) packet with given payload"""
        ip_packet = IPPacket(source=self.local_addr, dest=destination, payload=payload)
        return self.send2(ip_packet.build())

    def layer3recv(self, buffer_size: int):
        """Receive payload transferred in Layer 3 (IP) packet"""
        raw = self.recv2(buffer_size)
        pkt = IPPacket.parse_header(raw)
        return pkt.data
