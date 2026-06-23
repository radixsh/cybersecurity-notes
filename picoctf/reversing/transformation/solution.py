'''
Completed 2026-03-25

ord() and chr() are opposites, turning ASCII characters to numbers and vice
versa.
'''

with open("enc", "r") as f:
    flag = f.read()
    text = ""
    for i in range(0, len(flag)):
        val = ord(flag[i])
        print(bin(val))

        first = val >> 8
        print(bin(first))

        second = val & 0x00ff
        print(bin(second))

        print(chr(first), chr(second))
        text += chr(first)
        text += chr(second)

    print(text)
