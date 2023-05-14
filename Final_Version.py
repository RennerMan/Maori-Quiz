import random

# A list of Maori and their corresponding English numbers
NUMBERS = [["tahi", "one"], ["rua", "two"], ["toru", "three"], ["wha", "four"],
           ["rima", "five"], ["ono", "six"], ["whitu", "seven"],
           ["waru", "eight"], ["iwa", "nine"], ["tekau", "ten"]]

random.shuffle(NUMBERS)


# My Statement Formatter V3 Function
def statement_formatter(symbol, statement):
    # Putting the symbol around the sides of the text twice
    sides = symbol * 2
    # Printing the formatted statement with the symbols around the statement
    formatted_statement = f"{sides}{statement}{sides}"
    # Putting symbols around the top of the code
    bottom_top = symbol * len(formatted_statement)
    return f" {bottom_top}\n {formatted_statement}\n {bottom_top}"


# My Player Details V3 Functions
def name_finder():
    name = input("What is your name?")
    return name


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


# My Instructions V3 Function (With instructions this time)
def played_before():
    print(statement_formatter("#", "Welcome to the Maori Quiz!"))
    print()
    reply = input("Have you done this quiz before?\
    (Please answer yes or no)").lower()
    if reply == "yes" or reply == "y":
        print("Nice! We'll send you straight into the quiz")
        return "yes"
    elif reply == "no" or reply == "n":
        print(statement_formatter("?", "Instructions"))
        print()
        print("You will be given 10 random questions\
 about Maori Numbers up to 10")
        print()
        print("Try your best, we will show you how many questions\
 you got right out of 10")
        print()
        print(statement_formatter("!", "Good Luck"))
        print()
        print(statement_formatter("#n"
                                  "", "Quiz Time"))
        return "no"
    # Checking to make sure user provides a suitable response
    else:
        print("Please answer either 'yes' or 'no'")


response = played_before()


# My Quiz Questions V3 Function
# Combined with my score and length variables

def questions():
    # Defining the length and score variables
    length = 0
    score = 0
    while length != 10:
        for i in NUMBERS:
            question = input(f"What is {i[1]} in Maori?").lower().split()
            length += 1
            if question == i[0].lower().split():
                print(statement_formatter("!", "Correct Answer!"))
                score += 1
            else:
                print("Incorrect! You'll get it next time!")
    return score


test = questions()
print(statement_formatter("-", f"Game Over! You got {test}/10 questions right!"))
