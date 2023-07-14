import numpy as np


def packU16LittleEndian(source, destination):
    destination.append(source & 0xFF)
    destination.append((source >> 8) & 0xFF)


def packU32LittleEndian(source, destination):
    destination.append(source & 0xFF)
    destination.append((source >> 8) & 0xFF)
    destination.append((source >> 16) & 0xFF)
    destination.append((source >> 24) & 0xFF)


def unpackU16LittleEndian(index, source):
    try:
        return (source[index+1] << 8) | source[index]
    except IndexError:
        print("IndexError: Tried reading out of bounds of destination array")
        return


def unpackU32LittleEndian(index, source):
    try:
        return (source[index+3] << 24) | (source[index+2] << 16) | (source[index+1] << 8) | source[index]
    except IndexError:
        print("IndexError: Tried reading out of bounds of destination array")
        return
