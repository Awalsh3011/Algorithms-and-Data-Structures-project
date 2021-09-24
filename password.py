password = []

def set_password(word):
    global password
    length = len(word)
    contains_spaces = False
    for i in range(length):
        # use append function to add to list each time
        password.append(word[i])
        # Words that contain spaces are invalid
        if word[i] == ' ':
            contains_spaces = True

    if contains_spaces == True:
        password = []
        print('Password cannot contain spaces. Try again.')

    return password

def get_password_string():
    global password
    password_str = ''
    length = len(password)
    for i in range(length):
        # use the plus below to add each letter into the list
        password_str = password_str + password[i]
    
    return password_str


def add_special_symbol(symbol):
    global password
    #use if statement to see if the symbol are the required ones or not
    if symbol == '$' or symbol == '#':
        password.insert(0, symbol)
        password.append(symbol)
    else:
        print('Symbol must be $ or #. Try again.')

    return password

def convert_to_numbers():
    global password
    # use a loop to search through the password to look for the values
    for i in range(len(password)):
        if password[i] == 'S' or password[i] == 's':
            password[i] = '5'
        elif password[i] == 'O' or password[i] == 'o':
            password[i] = '0'

    return password