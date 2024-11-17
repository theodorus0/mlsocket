import os

from l2socket_windows import L2SocketWindows

if os.name == "nt":
    class Layer2Socket(L2SocketWindows):
        """OS-independent Layer 2 (Ethernet) socket"""
        pass
else:
    raise NotImplementedError("mlsocket work only on Windows at this moment")
