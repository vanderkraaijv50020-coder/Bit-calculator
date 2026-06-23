# generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")



# display instructions
def instruction():
    statement_generator("Instructions", "-")

    print('''
-Please enter your file type

-then answer all questions correctly

-if you want to exit please enter xxx when asked for file type
    ''')


# asks users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("file type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text
        elif response in ["text", 'txt', 't']:
            return "text"

        # if the response is invalid output an error
        else:
            print("Please enter a valid file type")

# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low ):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def img_check(question, low ):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
# calculates how many bits are needed to represent and integer
def image_calc():
    # Get the image dimensions
    height = img_check("Height:", 1)
    width = img_check("Width:", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# calculates how many bits are needed to represent and integer
def integer_calc():
    # Ask the user to enter an integer (more than/ equal to 0)
    integer = int_check("Integer:", 0)

   # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)


    # set up answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it"

    return answer

# Calculates number of bits needed to represent text in ascii
def calc_text_bits():

    # Get text from user
    response = input("Enter some text: ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters. "
              f"\nWe need {num_chars} x 8 bits to represent it "
              f"\nwhich is {num_bits} bits")

    return answer


# Main routine goes here

#display instructions if requested
want_instructions = input("press <enter> to read the instructions"
                          "or any key to continue")

if want_instructions == "":
    instruction()

while True:
    file_type = get_filetype()


    if file_type == "xxx":
        break

    # if users chose 'i' ask if they want an image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)