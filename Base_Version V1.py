import random

NUMBERS = [["tahi", "one"], ["rua", "two"], ["toru", "three"], ["wha", "four"], ["rima", "five"], ["ono", "six"],
           ["whitu", "seven"], ["waru", "eight"], ["iwa", "nine"], ["tekau", "ten"]]
random.shuffle(NUMBERS)

for i in NUMBERS:
    question = input(f"What is {i[1]} in Maori? ")
    if question == i[0]:
        print("Correct answer!")
    else:
        print("Incorrect :( The correct answer is", i[0])