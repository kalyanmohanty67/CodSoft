#Task : Python program for password Generator

import string
import random

length= eval(input(" Enter the length of the password :"))

lower= string.ascii_lowercase
upper= string.ascii_uppercase
n= string.digits
symbols= string.punctuation

Entire = lower + upper + n + symbols

temp = random.sample(Entire,length)

password = ''' '''.join(temp)

print( 'password' ,password)

exit()