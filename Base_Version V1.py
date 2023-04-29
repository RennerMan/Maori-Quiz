
# Base version V1. Testing code without functions to see what it might look like.
# Created by James Renner.

# Making a random number, then printing the corresponding list no.


import random
E_NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
NUMBERS = ["tahi", "rua", "toru", "wha", "iwa", "ono", "whetu", "waru", "iwa", "tekau"]
rand_num = random.randint(0,9)
question = input(f"What is {rand_num} in Maori?")
print(NUMBERS[rand_num])
answer =


if question == answer:
    print("Yay! you got it right!")
else:
    print("incorrect :( you'll get it next time")
    print(question)


