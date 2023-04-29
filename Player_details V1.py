# Component 2: Player details-gets players details to check they are around the right age for the quiz.
# Asks player what their name is
name = input("What is your name?")
print()
# Asks player what their age is
age = int(input(f"Hi {name}, what is your age?"))
# Checking they are around the appropriate age
if age <= 12:
    print("You might not be the right age for this quiz.")
    print("You can still take it though!")
elif age <= 9:
    print("You might not be the right age for this quiz.")
    print("You can still take it though!")
else:
    print("You are the right age for this quiz!")


