# Component 2: Player details V3-put v2's functions together
# So that the code is shorter and more concise
# Made by James Renner


# Asks player what their name is
def name_age():
    name = input("What is your name?")
    age = int(input(f"Hi, what is your age?"))
    # Checks they are the right age
    if 9 <= age <= 12:
        print("You are around the right age for the quiz!")
    else:
        print("You might not be the right age for this quiz.")
        print("You can still take it though!")
    return name


print(name_age())
