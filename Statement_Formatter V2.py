# Statement Formatter V2- Putting the Statement Formatter code into a function. Created by James Renner

# Setting up the Statement Formatter function
def statement_formatter(symbol, statement):
    sides = symbol * 2
    formatted_statement = f"{sides}{statement}{sides}"
    bottom_top = symbol * len(formatted_statement)
    return f" {bottom_top}\n {formatted_statement}\n {bottom_top}"


# Setting up a simple function to give space between print statements.
def space():
    print()


# Printing some pre-assigned sentences to check that the code works as intended
print(statement_formatter("#", "Welcome to the Maori Quiz!"))
space()
print(statement_formatter("?", "Instructions"))
space()
print(statement_formatter("!", "Correct Answer"))
space()
print(statement_formatter("*", "Goodbye!"))
