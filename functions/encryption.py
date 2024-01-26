import os

offset = int(os.getenv("DUMA"))


def encode_id(user_id):
    return "".join([chr(int(digit) + offset) for digit in str(user_id)])


def decode_id(user_id: str):
    return "".join([str(ord(c) - offset) for c in str(user_id)])
