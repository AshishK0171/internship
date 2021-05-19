"""
A receptionist has the duty of noting the details of visitors walking-in to the office. She notes in the register their name, phone number, place coming from and
body temperature. In a view to change this pen-paper task to a computer task, use your python programming skills to make a solution for this operation.
"""
from datetime import date
from datetime import datetime
import os
filename=str(date.today())+'.txt'#date as filename
line='-'*40
x=open(filename,'a')
if os.stat(filename).st_size == 0:
    x.writelines("\n CUSTOMER INFORMATION \n \n")#giving document heading if the document is empty

while True:
    cont=input('do you want to continue (y/n)')
    if cont.lower()=='n':
        break
    print('Enter the details')
    name=input('Enter name ')
    phno=input('Enter phone number ')
    origin=input('Enter the place coming from ')
    body_temp=input('Enter body temperature in celcius ')
    now = datetime.now()
    x.writelines('\nTime: '+str(now.strftime("%H:%M:%S")))
    x.writelines('\n '+'{0:16}: {1}\n {2:16}: {3}\n {4:16}: {5}\n {6:16}: {7} Celcius'.format('Name',name,'Ph-no',phno,'Origin',origin,'Body temperature',body_temp)+'\n'+line )

x.close()
x=open(filename,'r')

print('\nFile name '+filename+'\n'+x.read())

