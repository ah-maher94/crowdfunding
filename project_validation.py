from datetime import datetime
import main


def validate_info(project_info):
    if not (check_string_length(project_info['title'])):
        print('Title cannot be empty')
        return False
    elif not (check_project_exists(project_info['title'])):
        print('Project already exists')
        return False  
    elif not (check_string_length(project_info['details'])):
        print('Detials cannot be empty')
        return False
    elif not (validate_date(project_info['start_time']) and validate_date(project_info['end_time'])):
        print('Incorrect date format, should be DD-MM-YYYY')
        return False      
    else:
        return True    




def validate_date(project_date):
    try:
        datetime.strptime(project_date, '%d-%m-%Y')
        return True
    except:
        return False




def check_string_length(input_string):
    return len(input_string.strip())




def check_project_exists(title):
    projects = open('projects.txt', 'r')
    for project in projects:
        project_info = project.split(', ')
        project_title = project_info[1]
        project_owner = project_info[0]
        if(main.current_user_email.lower() == project_owner.lower() and project_title.lower() == title.lower()):
            return False
    return True
