# Component 5: Score Tracker V2-Put code into a function to use in final code


import random

# A list of Maori numbers and their corresponding english numbers
NUMBERS = [["toru", "three"]]

# Putting the lists in a different order
random.shuffle(NUMBERS)
# Selects the english half of the list and asks what the english word of the list is in Maori




def scorelength():
    length = 0
    score = 0
    while length != 10:
        for i in NUMBERS:
            question = input(f"What is {i[1]} in Maori?").lower().split()
            length += 1
            if question == i[0].lower().split():
                print("Correct answer!")
                score += 1
                return score
            else:
                print("Incorrect! You'll get it next time!")
test = scorelength()


print(f"Game Over! You got {test}/10 questions right!")
