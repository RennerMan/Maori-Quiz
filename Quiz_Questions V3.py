# Component 4: Quiz Questions-Asks player what a maori number is from the list
# Put code into a function for ease of use in final code


import random
# A list of Maori numbers and their corresponding english numbers
NUMBERS = [["toru", "three"]]
# Putting the lists in a different order
random.shuffle(NUMBERS)
# Selects the english half of the list and asks what the english word of the list is in Maori


def questions():
    for i in NUMBERS:
        question = input(f"What is {i[1]} in Maori?").lower().split()
        if question == i[0].lower().split():
            print("Correct answer!")
        else:
            print("Incorrect! You'll get it next time!")


print(questions())
print(questions())
print(questions())
print(questions())
