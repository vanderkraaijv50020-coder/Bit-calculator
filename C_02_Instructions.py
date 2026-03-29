# generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# display instructions
def instruction():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- instruction 1
- instruction 2
- etc   
    ''')


# Main routine goes here

# Display instructions if requested
want_instructions = input("press <enter> to read the instructions"
                          "or any key to continue")

if want_instructions == "":
    instruction()

print("program continues")
