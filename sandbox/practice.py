"""This is an interactive UNC basketball game program based off of a game from Feb 8th, 2018."""

from random import randint

def main() -> None:
    """Entrypoint of program."""
    global points
    points = 0
    print(greet())
    print(choice1())
    print(choice2())
    print(choice3())
    print(end())
    global player
    EMOJI = "\U0001F622 \U0001F627 \U0001F973 \U0001F40F \U000026F9 \U0001F93E \U0001F3C0"


def greet() -> None:
    """Greetings"""
    global player
    print(f"Hello new UNC men's basketball player! \U000026F9")
    print("Tonight we play Duke, our rivals.")
    print("We need your help to win.")
    print("Make the right choices and we WILL rush Franklin tonight!!\n")
    player = input("What is your name? ")
    return(f"Hello { player }! Here's the ball, get on the court! \U0001F3C0 \n")
    
    


def choice1()-> None:
    """Returns a choice."""
    #Choices are case-sensitive, type as shown
    print("In this game, you have to act quick!")
    global points
    global player
    choice1 = input("Shoot a three or pass to Luke Maye or throw the ball to Ramses? ")
    if choice1 == "Shoot a three":
        points = points + 1
        return(f"You missed \U0001F622. Duke rebounds. RUN back { player }!")
    else:
        if choice1 == "pass to Luke Maye":
            points = points + 2
            return("Score! Up two points.")
        else:
            if choice1 == "throw the ball to Ramses":
                points = points + 0
                print(f"Ramses is not on the team!? OH NO! You caused a turnover. Coach Williams is calling you \U0001F627. Get on the bench.\n")
                print(f"Your game is over champ, better luck next time { player }.")
                print(f"You scored { points } points.")
                start_over = input( "Would you like to play again? Y or N ? \n")
                if start_over == "Y":
                    return (main())
                else:
                    if start_over == "N":
                        quit()
    


def choice2() -> str:
    """Returns a random choice."""
    global player
    global points
    print(f"You are playing a great game { player }! Keep it up!! \n")
    choice2 = randint(1, 400)
    if choice2 < 100:
        points = points + 3
        return "You have stolen the ball from Grayson Allen! He is now crying. Great job! \n"
    else:
        if choice2 < 200:
            points = points + 5
            return "Theo Pinson passed you the ball. Slam Dunk!! \U0001F93E \n"
        else:
            if choice2 < 300:
                points = points + 2
                return "Wendell Carter Jr. fouls you. Time to make a free throw, I hope you have been practicing. \n"
            else:
                if choice2 < 400: 
                    points = points + 4
                    return "Timeout! Drink some water, you are playing a great game. \n"
    return choice2

def choice3()-> None:
    """Returns a final choice."""
    global player
    global points
    print(f"We have two minutes left in the second half. It all comes down to this. We need you { player }! Play smart.")
    choice1 = input("Pass to Joel Berry or throw the ball from half court or foul Grayson Allen? \n")
    if choice1 == "Pass to Joel Berry":
        points = points + 3
        print("Joel Berry scores! Great teamwork! \n")
    else:
        if choice1 == "throw the ball from half court":
            points = points + 10
            print("You made it! You are lucky, Coach Williams would not have been happy if you missed. \n")
        else:
            if choice1 == "foul Grayson Allen":
                points = points + 5
                print("Good foul. You stopped the clock. Allen misses, you rebound and throw to Platek down the court, score!! \n")
    return(f"You scored { points } points { player }.")
    
    


def end()-> None:
    global player
    global points
    
    print(f"Carolina Victory! 82-78! Awesome job { player }. What are you still doing here? Let's go to Franklin!! \U0001F973 \U0001F40F")
    quit()
    







if __name__ == "__main__":
    main()   