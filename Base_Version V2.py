import random

NUMBERS = [["tahi", "one"], ["rua", "two"], ["toru", "three"], ["wha", "four"], ["rima", "five"], ["ono", "six"],
           ["whitu", "seven"], ["waru", "eight"], ["iwa", "nine"], ["tekau", "ten"]]
random.shuffle(NUMBERS)
rounds = 0
right_answers = 0
while rounds != 10:
    for i in NUMBERS:
        question = input(f"What is {i[1]} in Maori? ")
        rounds += 1
        if question == i[0]:
            print("Correct answer!")
            right_answers += 1
        else:
            print("Incorrect :( The correct answer is", i[0])
print("Game over! 10 rounds played!")
print(f"You got {right_answers}/10 questions right")
