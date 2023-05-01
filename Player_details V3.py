# Component 2: player details-put v1's name and age data into a function
# You can then call this function multiple times in your code.
# Made by James Renner


# Asks player what their name is
def name_finder():
    name = input("What is your name?")
    return name


# Asks player what their age is
def age_finder():
    name = name_finder()
    age = int(input(f"Hi {name}, what is your age?"))
# Checks they are the right age
    if 9 <= age <= 12:
        print("You are around the right age for the quiz!")
    else:
        print("You might not be the right age for this quiz.")
        print("You can still take it though!")
    return age

print(age_finder())
print(age_finder())
print(age_finder())
