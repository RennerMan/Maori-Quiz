# Component 2: Player details V3-put v2's functions together
# So that the code is shorter and more concise
# Also stopped the code from breaking if anything non integer is entered

# Asks player what their name is


def name_age():
    name = input("What is your name?")
    while True:
        # Keeps trying an age until it receives a valid age
        try:
            age = int(input(f"Hi {name}, what is your age?"))
        # If the age is valid, it breaks the loop
            break
        # If it isn't, it tells the player it wasn't valid.
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
    # Checks they are the right age
    if 9 <= age <= 12:
        print("You are around the right age for the quiz!")
    else:
        print("You might not be the right age for this quiz.")
        print("You can still take it though!")
    return name


print(name_age())
