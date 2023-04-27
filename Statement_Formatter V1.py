# Statement Formatter V1- formatting text so that it stands out. Created by James Renner

# Setting up the words and symbols to format
text = input("type a sentence to format:")
symbol = input("type a symbol you want around your text:")

# Putting the assigned symbol twice on both sides
sides = symbol * 2
formatted_statement = f"{sides}{text}{sides}"
bottom_top = symbol * len(formatted_statement)

# Printing the formatted statement
print(bottom_top)
print(formatted_statement)
print(bottom_top)
