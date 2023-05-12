# Statement Formatter V3- Putting the Statement Formatter code into a function. Created by James Renner

# Setting up the Statement Formatter function
def statement_formatter(symbol, statement):
# Putting the symbol around the sides of the text twice
    sides = symbol * 2
# Printing the formatted statement with the symbols around the statement
    formatted_statement = f"{sides}{statement}{sides}"
# Putting symbols around the top of the code
    bottom_top = symbol * len(formatted_statement)
    return f" {bottom_top}\n {formatted_statement}\n {bottom_top}"


# Setting up the sentence and symbol you want to format
sentence = input("type a sentence to format:")
symbol_ = input("type a symbol you want around your text:")
# printing your formatted statement with the chosen symbol and sentence
print(statement_formatter(symbol_, sentence))
