import random
#word


#Predetermine a puzzle to find words from, making the variable set. 

puzzle=("adifloatpu"+
        "yopxednins"+
        "mspfycnnal"+
        "xeaeeungei"+
        "slufryerlc"+
        "abeeiascoi"+
        "buclqttbon"+
        "gojliviobg"+
        "admyahnerj"+
        "stringgvrs"+
        "djdyadefah")

points = 0
#points for puzzle system depending on guess.

####################################################################
#set indexing positions for the puzzle. This shows the user what to guess for the position of the word
def display_puzzle():
    print("")
    print("   0123456789")
    print("0 ",puzzle[0:10])
    print("1 ",puzzle[10:20])
    print("2 ",puzzle[20:30])
    print("3 ",puzzle[30:40])
    print("4 ",puzzle[40:50])
    print("5 ",puzzle[50:60])
    print("6 ",puzzle[60:70])
    print("7 ",puzzle[70:80])
    print("8 ",puzzle[80:90])
    print("9 ",puzzle[90:100])
    print("10",puzzle[100:])
##################################################################
       #Set questions and answers for the user to guess. We set a random generator later. 
question_list =["data type that holds a fractional value ","allows a loop to take place if something is true\false\equals another thing",
                "function checking another thing for truth in the statement","two constant objects False and True",
                "a function inside of another function","symbols carrying out arithmetic computation",
                "a line of characters","used to extract parts of a string",
                "position within a string or list starting at 0 and excluding the last character","set a specific name for a function"]
answer_list = ["float", "while", "if", "boolean", "nesting", "operators","string","slicing", "index","def"]




################################################################
#Set a function asking for the input answer to the question. This determines if the answer matches the answer to the question.
#The questions are set up in the order the answers are. 
def wordsearch(answer,puzzle):
       while True: #This sets the function to loop until found to be false. When it's false, the code subtracts an attempt from the 3
                            #given number of attempts, and loops.
              global points
              attempts =3
              display_puzzle()
              word1 = input("enter the index positions of "+answer+" followed by commas (EX.'2,3,4,5,6,')")
              #sets a variable to the input for the user and use in the project. When the user inputs a value, the value is assigned to the variable.
              foundword = ""
              index=""
              
              for i in word1:
                     
                     if i == ",":
                         if i.isdigit()==True:
                            i=int(index)
                            foundword += puzzle[i]
                            index=""
                            continue
                     
                     else:
                            index+=i
              if foundword == answer:
                     points = points +(attempts*1)
                     print ("thats correct")
                     break
              else:
                     attempts-=1
                     print("wrong")
#When an input is processed, and the guess is wrong, and the user loses a point.
##################################################################
#Ask a question and request the user's input. 
def question(question_list,answer_list):
       x=random.randrange(len(question_list))
       question=question_list[x]
       answer=answer_list[x]
       while True:
              global points
              attempts =10
              userresp = input(question)
              if userresp == answer:
                     points = points +(attempts*1)
                     print ("thats correct")
                     del question_list[x]
                     del answer_list[x]
                     return answer
              else:
                     attempts-=1
                     print("wrong")

##################################################################
                     #This is the main function which begins the program . It calles to the wordsearch function when the code reaches it,
                     #pushing the function to start. 

def main():
       while len(question_list) >0:
              answer=question(question_list,answer_list)
              wordsearch(answer,puzzle)

##################################################################







#We call the main function to start it. It will call another function.
main()

input("enter to exit")
















