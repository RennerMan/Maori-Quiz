# Component 3: Instructions V1- ask player if they have played quiz before
# Ask player if they have played before
played_before = input("Have you done this quiz before? (Please answer yes or no)")
if played_before == "yes":
    print("No instructions are given")
elif played_before == "no":
    print("Instructions given")
# Checking to make sure player provides a suitable response.
else:
    print("Please answer either 'yes' or 'no'")
