import random

# A 2-dimensional list of Maori and their corresponding English numbers


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


# My Player Details V3 Function
# Now checks to see if the name is valid
# Rearranged the code to make more sense


def name_age():
    while True:
        try:
            # Asks player what their name is
            name = input("What is your name?").lower().strip()
            # Creates a loop to check the name is valid
            if name.isalpha():
                # If the name is valid, it asks the player's age
                while True:
                    try:
                        # Loops until the age is valid
                        age = int(input(f"Hi {name}, what is your age?"))
                        if 9 <= age <= 12:
                            print("You are around the right age for the quiz!")
                        else:
                            print("You might not be the right age for this quiz.")
                            print("You can still take it though!")
                        return name  # Exit the function if both name and age are valid
                    except ValueError:
                        print("<error> Please enter a valid integer")
            # If the name isn't valid, it loops back until it is
            else:
                print("<error> Please enter a valid text")
        except ValueError:
            print("<error> Please enter a valid text")


# My Instructions V3 Function (With instructions this time)
# Welcomes player to quiz with their name to make it feel more personal


def played_before():
    print(statement_formatter("#", f"{name_age()},\
 Welcome to the Maori Quiz!"))
    print()
    reply = ""
    while reply != "yes" or "y" or "no" or "n":
        reply = input("Have you done this quiz before?\
    (Please answer yes or no)").lower().strip()
        # Creates a loop to check the reply is valid
        if reply == "yes" or reply == "y":
            print("Nice! We'll send you straight into the quiz")
            print(statement_formatter("#", "Quiz Time"))
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
            print(statement_formatter("#", "Quiz Time"))
            return "no"
        # Checking to make sure user provides a suitable response
        else:
            print("Please answer either 'yes' or 'no'")


response = played_before()


def played_before():
    print(statement_formatter("#", f"{name_age()}, Welcome to the Maori Quiz!"))
    print()
    reply = ""
    while reply != "yes" or reply != "y" or reply != "no" or reply != "n":
        reply = input("Have you done this quiz before? (Please answer yes or no)")
        reply = reply.lower().strip()  # Convert the input to lowercase and remove leading/trailing spaces
        # Creates a loop to check the reply is valid
        if reply == "yes" or reply == "y":
            print("Nice! We'll send you straight into the quiz")
            print(statement_formatter("#", "Quiz Time"))
            return "yes"
        elif reply == "no" or reply == "n":
            print(statement_formatter("?", "Instructions"))
            print()
            print("You will be given 10 random questions about Maori Numbers up to 10")
            print()
            print("Try your best, we will show you how many questions you got right out of 10")
            print()
            print(statement_formatter("!", "Good Luck"))
            print()
            print(statement_formatter("#", "Quiz Time"))
            return "no"
        # Checking to make sure user provides a suitable response
        else:
            print("Please answer either 'yes' or 'no'")


# My Quiz Questions V3 Function
# Combined with my score and length variables


def questions():
    # Defining the length and score variables
    length = 0
    score = 0
    # Creating a loop to ensure the quiz is 10 questions long
    while length != 10:
        for i in NUMBERS:
            # Asks the player what the english half of the list is in Maori
            question = input(f"What is {i[1]} in Maori?").lower().split()
            length += 1
            # If player answer matches up with the maori half of the list
            # It tells the player that they got the answer right
            if question == i[0].lower().split():
                print(statement_formatter("!", "Correct Answer!"))
                score += 1
            # If it doesn't, tells them it was incorrect
            else:
                print(f"Incorrect! It was {i[0]}!\
 You'll get it next time!")
    return score


# Getting the score variable outside the questions function


test = questions()
# Tells the player how many questions they got correct out of ten
print(statement_formatter("-", f"Game Over!\
You got {test}/10 questions right!"))
print()
print("For revision, these are the maori numbers up to 10:")
print()
print("Tahi, Rua, Toru, Wha, Rima, Ono, Whitu, Waru, Iwa, Tekau")
