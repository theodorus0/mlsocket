import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(("1.1.1.1", 0))
    local_ip = s.getsockname()[0]
