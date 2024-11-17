from pydivert import WinDivert, Packet, Direction

from iptools import local_ip
from l2socket_base import Layer2SocketBase


class L2SocketWindows(Layer2SocketBase):
    __divert: WinDivert

    def __init__(self):
        self.__divert = WinDivert(f"ip.DstAddr == {local_ip} || ip.SrcAddr == {local_ip}")
        self.__divert.open()

    def recv2(self, buffer_size: int):
        pkt = self.__divert.recv(buffer_size)
        return pkt.raw.tobytes()

    def send2(self, payload: bytes) -> int:
        pkt = Packet(payload, (9, 0), Direction.OUTBOUND)
        return self.__divert.send(pkt)

    def __del__(self):
        self.__divert.close()
        print("WinDivert closed")
