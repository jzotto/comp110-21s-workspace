
global points
points = 0
while True:
    loop = input("Now, pass to Platek or pass to B-Rob or quit? ")
    if loop == "pass to Platek":
        points += 3
        print(f"Platek is blocked! Recover , find an opening! You have scored points so far! \n")
    else:
        if loop == "pass to B-Rob":
            points += 3
            print("Nice pass, B-Rob makes a three!")
            break
        else:
            if loop == "quit":
                quit()

