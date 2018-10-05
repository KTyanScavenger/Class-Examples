


def test_scores():
    print("What were your last ten test scores? ")
    #get the sum of the test scores
    t1=float(input("Test 1:"))
    t2=float(input("Test 2:"))
    t3=float(input("Test 3:"))
    t4=float(input("Test 4:"))
    t5=float(input("Test 5:"))
    t6=float(input("Test 6:"))
    t7=float(input("Test 7:"))
    t8=float(input("Test 8:"))
    t9=float(input("Test 9:"))
    t10=float(input("Test 10:"))

    av_sum=(t1+t2+t3+t4+t5+t6+t7+t8+t9+t10)
    avg=av_sum/10
    if avg>=90.0:
        print("You have an A! Great job! Keep it up!", avg,"%")
    else:
        if avg>=80.0:
            print("You have a B! Nice work.", avg,"%")
        else:
            if avg>=70.0:
                print("You have a C! You could do better.", avg,"%")
            else:
                if avg>= 60.0:
                    print("You have a D! Try harder!", avg,"%")
                else:
                    if avg>=50.0:
                        print("You have an F! Fix your grade!", avg,"%")
                    else:
                            print("Something went wrong.")

test_scores()


print("END")
                                
