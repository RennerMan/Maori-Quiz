# Base version V1. Testing code without functions to see what it might look like.
# Created by James Renner


import random
# Making a random number, then printing the corresponding list no.
rand_num = random.randint(0,9)
NUMBERS = ["tahi", "rua", "toru", "wha", "iwa", "ono", "whetu", "waru", "iwa", "tekau"]

question = input(f"What is {rand_num} in Maori?")
answer = (NUMBERS[rand_num])
if question == answer:
    print("Yay! you got it right!")
else:
    print("incorrect :( you'll get it next time")


