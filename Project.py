#Kyla Ryan and Parker Dean
#Nov 2018
#P.1/2

import random
import os

#import system
def menu():
    #determines what the user wants to do
    print("MENU\n"
          "1.Play Number Guess\n"
          "2.Play Coin Toss\n"
          "3.View Credits\n"
          "4.Quit\n"
          "")
    option=input("What do you want to do? \n"
                 "Enter 1, 2, 3, or 4.\n"
                 "")
    #inputs from the user determine what they do
    if option=="1":
        num_guess()
    elif option=="2":
        coin_flip()
    elif option=="3":
        credit()
    elif option=="4":
        quit1()
    else:
        print("That is not a valid input.")
        menu()

#number guess name
def num_guess():
    low=0
    high=100
    #create random number
    set_num=random.randint(low,high)
    print("Guess a number between 1 and 100!\n"
          "")
    g1=int(input("Guess: "))
    #first guess
    if g1==set_num:
        print(""" __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
                                            
                                            """)
        what_now=input("What do you want to do now?\n"
                       "1.Guess Again.\n"
                       "2.Back To Menu.\n"
                       ""
                       "Enter 1 or 2."
                       "")
        if what_now=="1":
            num_guess()
        elif what_now=="2":
            menu()
        else:
            print("That is not a valid option.")
            what_now()
    else:
        print("Try again.")
        if g1>=set_num:
            print("Too high! Guess lower!")
        elif g1<=set_num:
            print("Too low! Guess higher!")
            #second guess
        g2=int(input("Guess: "))
        if g2==set_num:
            print(""" __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
                                            
                                            """)
            what_now=input("What do you want to do now?\n"
                       "1.Guess Again.\n"
                       "2.Back To Menu.\n"
                       ""
                       "Enter 1 or 2."
                       "")
            if what_now=="1":
                num_guess()
            elif what_now=="2":
                menu()
            else:
                print("That is not a valid option.")
                what_now()
        else:
            print("Try again.")
            if g2>=set_num:
                print("Too high! Guess lower!")
            elif g2<=set_num:
                print("Too low! Guess higher!")
                #third guess
            g3=int(input("Guess: "))
            if g3==set_num:
                print(""" __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
                                            
                                            """)
                what_now=input("What do you want to do now?\n"
                           "1.Guess Again.\n"
                           "2.Back To Menu.\n"
                           ""
                           "Enter 1 or 2."
                           "")
                if what_now=="1":
                    num_guess()
                elif what_now=="2":
                    menu()
                else:
                    print("That is not a valid option.")
                    what_now()
            else:
                print("Try again.")
                if g3>=set_num:
                    print("Too high! Guess lower!")
                elif g3<=set_num:
                    print("Too low! Guess higher!")
                    #fourth guess
                g4=int(input("Guess: "))
                if g4==set_num:
                    print(""" __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
                                            
                                            """)
                    what_now=input("What do you want to do now?\n"
                           "1.Guess Again.\n"
                           "2.Back To Menu.\n"
                           ""
                           "Enter 1 or 2."
                           "")
                    if what_now=="1":
                        num_guess()
                    elif what_now=="2":
                        menu()
                    else:
                        print("That is not a valid option.")
                        what_now()
                else:
                    print("Try again.")
                    if g4>=set_num:
                        print("Too high! Guess lower!")
                    elif g4<=set_num:
                        print("Too low! Guess higher!")
                        #fifth guess
                    g5=int(input("Guess: "))
                    if g5==set_num:
                        print(""" __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
                                            
                                            """)
                        what_now=input("What do you want to do now?\n"
                                       "1.Play Again.\n"
                                       "2.Back To Menu.\n"
                                       ""
                                       "Enter 1 or 2."
                                       "")
                        if what_now=="1":
                            num_guess()
                        elif what_now=="2":
                            menu()
                        else:
                            print("That is not a valid option.")
                            what_now()
                    else:
                        print("You didn't guess the number in your 5 tries.\n"
                              "The number was,",set_num,".")
                        what_now=input("What do you want to do now?\n"
                                       "1.Play Again.\n"
                                       "2.Back To Menu.\n"
                                       ""
                                       "Enter 1 or 2."
                                       "")
                        if what_now=="1":
                            num_guess()
                        elif what_now=="2":
                            menu()
                        else:
                            print("That is not a valid option.")
                            what_now()
#coin flip game
def coin_flip():
    flips = 0
    heads = 0
    tails = 0
    print("""
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \\
  /`       .-'~"-.       `\\
 ; L      / `-    \\      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \\ |        |
;        `~~;     \\\\        ;
 ;  INGODWE /      \\\\)P    ;
  \\  TRUST '.___.-'`"     /
   `\\                   /`
     '._   1 9 9 7   _.'
         `'-..,,,..-'`""")
#Asks for user's guess
    coin_guess = input("If i flip a coin 100 times, which do you think will be higher? Heads or Tails: ")
    #Flip loop
    while flips < 100:
        if random.randint(1,2) == 1:
            print("heads")
            heads += 1
        else:
            print("tails")
            tails += 1
        flips += 1
    if coin_guess.lower() == "heads":
        print("So you guessed Heads")
        print("There were" , heads , "Heads, and there were" , tails , "tails")
        #determines amount of guess for win or lose
        if heads > tails:
            print("You Win!")
        else:
            print("You Lose!")
    elif coin_guess.lower() == "tails":
        print("So you guessed Heads")
        print("There were" , tails , "Tails, and" , heads , "Heads")
        if heads < tails:
            print("You win!")
        else:
            print("You lose!")

    menu()

#terminate the program
def quit1():
    os._exit(0)

#Gives credit to the makers
def credit():
    print("Directed by: Parker Dean and Kyla Ryan")
    print("Written by: Parker Dean and Kyla Ryan")
    print("Inspired by: Eric Broadbent")

    menu()

                    
menu()    
                
                    
