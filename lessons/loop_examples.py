"""Examples using loops."""

count: int = 0
while input("Do you need more love? yes/no - ") == "yes":
    # Body block of while loop is evaluated
    #when the thest expression is truw
    print("I love you!")
    count += 1
    print(f" Count is {count}")

# Iterating a specific number of times
i: int = 0 # i is typicaclly short for index
iterations: int = 1000000

while i < iterations:
    if i % 1000 == 0:
        print(f"I love you! i: {i}")
    i += 1 # Important that this increment is NOT in the if statement 

print("Have a lovely day.")




