

hexchars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

hexchars.reverse()

badchars = ['00', 'd5', 'b1','4e','1a','13','12','0d','0c','0b','0a','00']
# ,'0a','0b','0c,','0d','0e','0f'

chars = ''

for firstchar in hexchars:
    for secondchar in hexchars:
        #char = '\\' + 'x' + str(firstchar) + str(secondchar)
        char = str(firstchar) + str(secondchar)
        if char not in badchars:
            chars += char


NOPs = '90909090909090909090'

print(chars)

rawdata = bytes.fromhex(chars)

with open("allchars.txt", "wb") as file:
    file.write(rawdata)

#print(rawdata)
