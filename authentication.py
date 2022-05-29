import user_validation
import projects

current_user_email = ''

def register():

    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    email = input('Email: ')
    password = input('Passowrd: ')
    password_confirmation = input('Confirm Password: ')
    phone = input('Phone(01xxxxxxxxx): ')

    user_info = {
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email,
        'password' : password,
        'password_confirmation' : password_confirmation,
        'phone' : phone,
    }

    if(user_validation.validate_info(user_info)):
        global current_user_email
        db = open('users.txt', 'a')
        db.write(f'{first_name}, {last_name}, {email}, {password}, {phone}\n')
        db.close()
        current_user_email = email
        print('Registered 👋')
    else:
        print('Try again!')
        register()





def login():
    email = input('Email: ')
    password = input('Password: ')
    db = open('users.txt', 'r')
    for user in db:
        user_info = user.split(', ')
        user_email = user_info[2]
        if(user_email.lower() == email.lower() and password == password):
            global current_user_email
            current_user_email = email
            print('Logged in 👋')
            break
    else:
            print('Wrong email or password, try again')
            display_menu()




def display_menu():
    print(f'Press 1 to Login | 2 to Register: ')
    try:
        user_input = int(input())
        if(user_input == 2):
            register()
        elif(user_input == 1):
            login()
        else:
            print('Invalid input, try again')
            display_menu()
    except:
        print('Invalid input, try again')
        display_menu()





display_menu()