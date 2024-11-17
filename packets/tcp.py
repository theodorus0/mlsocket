import struct
from collections.abc import Iterable
from enum import IntFlag


class TCPFlags(IntFlag):
    FIN = 0x01
    SYN = 0x02
    RST = 0x04
    PSH = 0x08
    ACK = 0x10
    URG = 0x20
    ECE = 0x40
    CWR = 0x80
    NS = 0x100


class TCPPacket:
    def __init__(self, *, src_port: int = 0, dest_port: int = 0,
                 seq: int = 0, ack: int = 0, window_size: int = 0,
                 flags: Iterable[TCPFlags] = None, data: bytes = b''):
        self.source_port = src_port
        self.destination_port = dest_port
        self.sequence_number = seq
        self.acknowledgment_number = ack
        self.data_offset = 5  # Default header length (5 * 4 = 20 bytes)
        self.reserved = 0
        self.flags = flags if flags is not None else []
        self.window_size = window_size
        self.checksum = 0
        self.urgent_pointer = 0
        self.options = b''
        self.data = data

    @staticmethod
    def parse_from_bytes(byte_data):
        packet = TCPPacket()

        # Unpack the fixed-size fields
        packet.source_port, packet.destination_port, packet.sequence_number, \
            packet.acknowledgment_number, header_and_flags, packet.window_size, \
            packet.checksum, packet.urgent_pointer = struct.unpack('!HHII4H', byte_data[:20])

        # Extract Data Offset (4 bits) and Reserved (3 bits) from the header_and_flags byte
        packet.data_offset = (header_and_flags >> 4) & 0xF
        packet.reserved = (header_and_flags >> 1) & 0x7

        # Extract Control Flags (9 bits) from the header_and_flags byte
        flags = header_and_flags & 0x1FF
        packet.flags = [flag for flag in TCPFlags if flag & flags]

        # Calculate the length of the options and data
        header_length = packet.data_offset * 4
        options_length = header_length - 20

        # Extract options and data
        if options_length > 0:
            packet.options = byte_data[20:20 + options_length]
        packet.data = byte_data[header_length:]

        return packet

    def build(self):
        # Combine Data Offset and Reserved into a single byte
        header_and_flags = ((self.data_offset & 0xF) << 4) | ((self.reserved & 0x7) << 1) | (sum(self.flags) & 0x1FF)

        # Pack the fixed-size fields
        header = struct.pack('!HHII4H',
                             self.source_port,
                             self.destination_port,
                             self.sequence_number,
                             self.acknowledgment_number,
                             header_and_flags,
                             self.window_size,
                             self.checksum,
                             self.urgent_pointer)

        # Combine header, options, and data
        return header + self.options + self.data
