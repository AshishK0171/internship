#program to encrypt the given message
msg=input('enter the message: ')
msg=msg.upper() #convert the msg alphabets to uppercase
lookup=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
encrypted=''
for x in msg:
    if x in lookup:
        y=lookup[(lookup.index(x)+3)%26]
        encrypted+=y
    else:
        encrypted+=x
print(msg+'\n'+encrypted)
