import re

def validate_info(user_info):
    fname_check = check_name_length(user_info['first_name'])
    lname_check = check_name_length(user_info['last_name'])
    if not (fname_check and lname_check):
        print('Invalid first name or last name, register again')
        return False
    elif not (check_phone(user_info['phone'])):
        print('Invalid phone number')
        return False
    elif not (check_password_length(user_info['password'])):
        print('Enter valid password, min 1 char')
        return False
    elif not (check_password_confirmation(user_info['password'], user_info['password_confirmation'])):
        print('Password confirmation doesnot match')
        return False
    elif(check_email(user_info['email'])):
        if(check_email_exists(user_info['email'])):
            print('Email already exists, register again')
            return False
        else:
            return True
    else:
        print('Invalid Email')
        return False


def check_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(email_regex, email)):
        return True
    else:
        return False


def check_name_length(user_name):
    return len(user_name.strip())


def check_email_exists(email):
    db = open('users.txt', 'r')
    for user in db:
        user_info = user.split(', ')
        print(user_info)
        user_email = user_info[2]
        if(user_email == email):
            return True
    return False


def check_password_length(password):
    return len(password.strip())


def check_password_confirmation(password, password_confirmation):
    return True if (password == password_confirmation) else False


def check_phone(phone):
    mobile_reges = r'\b01[0125][0-9]{8}\b'
    if(re.fullmatch(mobile_reges, phone)):
        return True
    else:
        return False