import sys

def is_hex(s):
    try:
        bytes.fromhex(s)
        return True
    except ValueError:
        return False

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <hex_data_or_string>")
    sys.exit(1)

input_data = sys.argv[1]

if is_hex(input_data):
    hex_data = input_data
else:
    hex_data = input_data.encode().hex()

data = bytes.fromhex(hex_data)

decoded = ""
for i, byte in enumerate(data):
    decoded_byte = byte - i
    if 32 <= decoded_byte <= 126:
        decoded += chr(decoded_byte)

print(decoded)