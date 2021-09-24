import password

selection = '0'
# use a while loop so it goes through all the options
# set it as not equal to 5 as 5 is the exit and when 5 is selcted the menu wont appear again
while selection != '5':

    print('1. Enter a new password')
    print('2. Display the current password')
    print('3. Add special symbol [$,#,%] as second and second-last characters')
    print('4. Replace all "s" characters with 5 and "o" characters with 0')
    print('5. Exit')
    selection = input('Choose option 1 - 5: ')

    if selection == '1':
        word = input('Enter a password')
        password.set_password(word)
    
    elif selection == '2':
        pw = password.get_password_string()
        print(f'Password: {pw}')


    elif selection == '3':
        special = input('Enter a special character $ or #: ')
        password.add_special_symbol(special)

    elif selection == '4':
        password.convert_to_numbers()
    

    
