###if contditionA<><=>= == =conditionB:
###else:


#Name and Age funciton
name=input("What is your name? ")
age=input("What is your age? ")

if name.isalpha() and name.istitle() and age.isdigit() and age<"25" or name== "Kyla":
    print("The name you entered was ",name+ ". Your age was ",age)
else:
    print("enter a valid name")


#Next example: Restriction function
age_a=int(input("What is your age? "))
if age_a < 65  or age_a > 16:
    print("You can drive!")
elif age_a>65:

    print("Sorry, you can't drive, you can't see.")
elif age_a>16:
    print("You need to grow up!")
else:
    print("You shouldn't be driving.")


##
##Sudo-Code
##num1:input from the user; cast to int
##num2:input from the user; cast to int
##check numbers if num1 and num2 are all digits
##If both are digits tel luser (compound if)
##If one or the other is a digit tell user
##If neither are digits tell user


num1=input("enter a number")
num2=input("enter a number")

if num1.isdigit() and num2.isdigit():
    print(num1,num2,"are both digits")
         
elif num1.isdigit() or num2.isdigit():
    print("only one of the numbers is a digit")
else:
    print("those are not digits")




