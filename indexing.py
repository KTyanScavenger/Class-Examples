#Kyla Ryan
#11/18
import random

name="Kyla Ryan"
length=len(name)
print(length)
index_pos=random.randrange(0,length)
#Both ends are inclusive.
char=name[-1]
print(char)
#index positioning. Each character has an index position. It starts at 0, as everything does in Computers.
if index_pos<=length:
    char=name[-1]
else:
    print ("That won't work.")
