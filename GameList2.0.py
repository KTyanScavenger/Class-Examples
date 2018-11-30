game_list=[]
while True:
    option=int(input("""
    1-Add a Game,
    2-Remove a Game,
    3-Insert a Game
    4-Exit (Quit)
    Make your choice.... 1,2, 3, or 4.....
    """))

    if option==1:
        print("The option allows you to add a game to your list.")
        print(game_list)
        game=input("What game would you like to add? ")
        game_list.append(game)
        print(game_list)

    elif option==2:
        print("This option allows you to remove a game from your list.")
        print(game_list)
        
        while True:
            game=input("Which game would you like to remove from your list? ")
            if game in game_list:
                game_list.remove(game)
                print(game_list)
                break
            else:
                print("That game is not in the list.")

    elif option==3:
        print("This option allows you to insert a game at a give position.")
        while True:
            game=input("What game would you like to insert? ")
            pos=int(input("What position would you like to insert it at? "))
            pos-=1
            if pos<len(game_list):
                game_list.insert(pos,game)
                print(game_list)
                break
            else:
                print("Invalid syntax.")
            
        
        
    if option==4:
        input("Press enter to exit.")
        break
