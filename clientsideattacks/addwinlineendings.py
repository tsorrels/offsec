import sys

filename = sys.argv[1]


clrfbytes = bytes.fromhex('0d0a')

writefile = open(filename + '_clrf', "wb") 

with open(filename, "r") as readfile:
    lines = readfile.readlines()
    for line in lines:
        linebytes = line.encode('utf-8')
        writefile.write(linebytes)
        writefile.write(clrfbytes)
        


writefile.close()
