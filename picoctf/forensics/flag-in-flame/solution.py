import base64
import sys

def log_to_base64():
    infile_name = sys.argv[1]
    outfile_name = "output.png"

    with open(infile_name, 'r') as infile:
        string = infile.read()

        b64 = base64.b64decode(string)
        with open(outfile_name, 'wb') as outfile:
            outfile.write(b64)

# Source - https://stackoverflow.com/a/77512455
# Posted by Olivier Lasne
# Retrieved 2026-03-25, License - CC BY-SA 4.0
def decode_hexstring(hexstring):
    decoded = ''
    for i in range(0, len(hexstring), 2):
        b = hexstring[i:i+2]
        b = b.decode() # it's a byte-string
        c = bytes.fromhex(b).decode('utf-8')
        print(b, c)
        decoded = decoded + c
    return decoded

def main():
    # This number comes from the PNG created by log_to_base64()
    flag = b"7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F62653836303237397D"
    print(decode_hexstring(flag))

main()
