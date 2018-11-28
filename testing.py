bday_survey=[]
bday=int(input("What was the day of the month you were born? (1-31) or q to finish. "))
if bday>31 or bday==0:
    print("Not a day of the month.")
while bday!="q":
    bday=int(input("What was the day of the month you were born? (1-31) or q to finish. "))
    if bday<=31 and bday>0:
        bday_survey.append(bday)
    if bday==str("q"):
        break
    if bday>31:
        print("Too large. Try again.")
print(bday_survey)
