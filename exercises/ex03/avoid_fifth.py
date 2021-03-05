"""EX03 - avoid_fifth function."""

__author__: str = "730163077"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(x: str) -> str:
    """This function will remove the character "e" or "E" from a string."""
    i: int = 0
    new_list: list[str] = []
    while  i < len(new_list):
        if i == "e" or "E":
           new_list.pop(i)
        else:
            new_list.append(i)
            i += 1
    return new_list

    


    #make a new list that is empty, then have a while loop and 
    #if it does not have an E it stays if it does have an E erase it    
    #need i += 1 to move to next letter

if __name__ == "__main__":
    main()