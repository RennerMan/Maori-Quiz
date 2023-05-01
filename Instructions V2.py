# Component 3: Instructions V2- Added additional responses for ease of use.
# Ask player if they have played before
played_before = input("Have you done this quiz before?\
 (Please answer yes or no)").lower()

if played_before == "yes" or played_before == "y":
    print("No instructions are given")
elif played_before == "no" or played_before == "n":
    print("Instructions given")
# Checking to make sure player provides a suitable response.
else:
    print("Please answer either 'yes' or 'no'")
print(f"You said {played_before}")
