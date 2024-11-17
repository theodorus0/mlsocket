from abc import abstractmethod


class Layer2SocketBase:
    @abstractmethod
    def recv2(self, buffer_size: int) -> bytes:
        """Receive payload transferred in Layer 2 (Ethernet) packet"""
        pass

    @abstractmethod
    def send2(self, buffer_size: int) -> int:
        """
        Send Layer 2 (Ethernet) packet with given payload
        :returns: Number of bytes actually sent
        """
        pass
