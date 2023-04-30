# Component 2: Player details-gets players details to check they are around the right age for the quiz.
# Asks player what their name is
name = input("What is your name?")

# Asks player what their age is
age = int(input(f"Hi {name}, what is your age?"))

# Checking they are around the appropriate age
if 9 <= age <= 12:
    print("You are around the right age for the quiz!")
else:
    print("You might not be the right age for this quiz.")
    print("You can still take it though!")
