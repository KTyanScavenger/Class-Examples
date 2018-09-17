#Kyla Ryan 
#9/18
#Get Name Function


def get_name():
    name=input("What is your name? ")


#display name
    print("The name you entered was", name)





print("This is our function")
#get_name()



def areaOfCircle(radius1):
    PI = 3.14159263
#1 Get a radius
    radius = radius1
    
    
#2 compute an area
    radius = float(radius)
    area = radius*radius*PI
#3 Display informaiton back
    print("The area of the circle is: ",area)
#inputx("What is radius? ")
#areaOfCircle(radiusx)


def pythagorean_theorum():
    #a^2+b^2=c^2
    a=float(input("what is side a of the triangle?"))
    b=float(input("what is side b of the triangle?"))
    c=a*a+b*b
    
    print("The third side is",c)

#pythagorean_theorum()


def pythagorean_theorum():
    #a^2+b^2=c^2
    a=float(ap)
    b=float(ap)
    c=a*a+b*b
    c=math.sqrt(c)
    
    print("The third side is",c)

ax=input("what is side a of the triangle?")
ax=input("what is side b of the triangle?")
#pythagorean_theorum(ax,bx)



def add_numbers():
    num1=input("enter a number")
    num2=input("enter a second number")
    num3=int(num1)+int(num2)
    return num3
#print("the sum of your numbers is: ",num4)
#num4=add_numbers() #num4=num3
#print(num4)
#add_numbers()

def add_numbers(X,Y):
    num1=X
    num2=Y
    num3=int(num1)+int(num2)
    print("this is num1")
    print("this is num2")
    return num3
X=input("enter a number")
Y=input("enter a second number")
num4=add_numbers(X,Y) #num4=num3
print("the sum of your numbers is: ",num4)

print(num4)


def get_name(name_input):
    


#display name
   name=name_input
   name.lower()
   name=name.title()
   print("the name you entered was",name)
   print("is this correct? yes or no")



print("This is our function")
name=input("what is your name")
get_name(name)


