# Component 5: Score/Length Tracker V2:
# Put variable into a function to use in final code
import random

# A list of Maori numbers and their corresponding English numbers
NUMBERS = [["toru", "three"]]

# Putting the lists in a different order
random.shuffle(NUMBERS)


# Selects the English half of the list and asks what the English word of the list is in Maori
def score_length():
    # Introducing the length and score variables
    length = 0
    score = 0
    # Checking that the code won't run past 10 questions
    while length != 10:
        for i in NUMBERS:
            question = input(f"What is {i[1]} in Maori?").lower().split()
            # Increases length per question asked
            length += 1
            if question == i[0].lower().split():
                print("Correct answer!")
                score += 1
            # Increases score if question is correct
            else:
                print("Incorrect! You'll get it next time!")
    return score


# Making variable "test" the same as the function
# To access "score" outside the function
test = score_length()
print(f"Game Over! You got {test}/10 questions right!")
