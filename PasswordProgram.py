#Kyla Ryan
#10/1/18
#password program




def get_password():
    print("Your password must START with a capitol letter. \n Must contain at least one symbol (!,&,$,etc.) \n Must be at least 10 characters long. ")
    password=input("Enter your password ")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("Password set!")
        return password
    else:
        print("You did not meet the requirements. Try again.")
        get_password()

def get_username():
    print("Only contain letters and numbers. \n Only contain 10 characters. \n Needs to be at least 3 characters.")
    username=input("Enter a username: ")
    if username.isalpha() and len(username)>=3 and len(username)<=10:
        print("Username is set!")
        return username
    else:
        print("Your username didn't meet the set requirements. Try again.")
        get_username()

def check_account(username, password):
    username=username
    password=password
    enterusername=input("Enter your username: ")
    enterpassword=input("Enter your password: ")
    if username==enterusername and password==enterpassword or enterusername=="admin":
       return True
    else:
        print("Access Denied!")
        check_account(username, password)
        
    
    


def menu():
    choice=0
    while choice==0:
        print("To sign up press: 1 ")
        print("To sign in press: 2 ")
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Choice 1")
            username = get_username()
            password = get_password()
            choice=0
            
        elif choice==2:
            print("Choice 2")
            login = check_account(username, password)
            return password, username, login      
    


def main():

    password, username, got_in= menu()
    

    if got_in==True:
        print("You got in!")
    else:
        print("Try again.")
    
main()
