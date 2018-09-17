#Kyla Ryan
#9/17

def test_average(total):
    my_list=[]
    total_score=int(total)
    count=0
    while count != total_score:
        score = float(input("enter a score:"))
        my_list.append(score)
        count=count+1
                            
    b=sum(my_list)
    avg=b/total_score
    print("your avg is",avg)


t=input("enter total tests")
test_average(t)




def my_average():
    t1=input("test 1:")
    t2=input("test 2:")
    t3=input("test 3")
