# Component 3: Instructions V3: Put code into a function for ease of use.
def played_before():
    reply = input("Have you done this quiz before? (Please answer yes or no)").lower()
    if reply == "yes" or reply == "y":
        print("No instructions are given")
        return "yes"
    elif reply == "no" or reply == "n":
        print("Instructions given")
        return "no"
# Checking to make sure user provides a suitable response
    else:
        print("Please answer either 'yes' or 'no'")

response = played_before()
print(f"You said {response}")
