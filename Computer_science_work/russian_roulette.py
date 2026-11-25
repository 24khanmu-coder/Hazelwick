import random
words = ["blank","blank","blank","blank","dead"]


print("hello freind time to play")
shell = random.choice(words)
while True:
    turn = input("i shoot now are u ready")
    if turn == "yes":
        print(shell)
    if shell == "dead":
        print("I win fool")
        break
    elif shell == ("blank"):
        print("i guess it your turn.Take the shotty you twat.SHOOT ME SHOOT ME NOW I WANT IT")
        shoot = input("Do you want to shoot")
        while shoot != "yes":
            print("I SAID KILL ME KILL ME NOW FOOL")
            shoot = input("Do you want to shoot")
        if shoot == "yes":
            print(shell)
    if shell == "dead":
        print("you have you have won ")
        break
    else:
        print("it seems i have gotten lucky my turn")
    print(shell)
    if shell == "blank":
        print("damit why wont u die")
    elif shell == "dead":
        print("you survived for longer than i thought but i remain undefeated")
        


