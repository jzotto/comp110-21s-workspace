"""EX03 - palindromify function."""

__author__: str = "730163077"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    palindromify("race", False)
    palindromify("han", True)
    palindromify("red", True)
    palindromify("live on time ", False)

    
def palindromify(x: str, y: bool) -> str:

if __name__ == "__main__":
    main()