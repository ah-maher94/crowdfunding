import sys
import project_validation
import authentication
from datetime import datetime

def display_projects_menu():
    print("""
    Choose from menu:
    1. add new project
    2. view all projects
    3. update your projects
    4. delete project
    5. search projects
    6. exit
    """)

    try:
        user_choice = int(input())
    except:
        print('Invalid input, try again')
    if(user_choice == 1):
        add_project()
    elif(user_choice == 2):
        list_projects()
    elif(user_choice == 3):
        edit_project()
    elif(user_choice == 4):
        delete_project()
    elif(user_choice == 5):
        search_project()
    elif(user_choice == 6):
        print('👋')
        exit()





def add_project(project_info = {}):
    action = 'Updated!👌'
    if not (project_info):
        action = 'Added! 👍'
        title = input('Title: ')
        details = input('Details: ')
        start_time = input('Start Time(DD-MM-YYYY): ')
        end_time = input('End Time(DD-MM-YYYY): ')

        project_info = {
            'title' : title,
            'details' : details,
            'start_time' : start_time,
            'end_time' : end_time,
        }

    if(project_validation.validate_info(project_info)):
        db = open('projects.txt', 'a')
        db.write(f"{authentication.current_user_email}, {project_info['title']}, {project_info['details']}, {250000}, {project_info['start_time']}, {project_info['end_time']}\n")
        db.close()
        print(action)

    display_projects_menu()




def edit_project():
    updated = False
    project_name = input('Enter project name: ')
    db = open('projects.txt', 'r')
    for project in db:
        project_info = project.split(', ')
        project_title = project_info[1]
        project_owner = project_info[0]
        if(authentication.current_user_email.lower() == project_owner.lower() and project_title.lower() == project_name.lower()):
            updated = True
            update_project(project_info)
    if not updated:
        print(f'Project {project_name} does not exist\n')
        print('Press 1 to retry, 2 to return to main menu: ')
        try:
            user_choice = int(input())
            if(user_choice == 1):
                edit_project()
            elif(user_choice == 2):
                display_projects_menu()
            else:
                print('Invalid input, Back to main menu')
                display_projects_menu()
        except:
            print('Invalid input, Back to main menu')
            display_projects_menu()





def update_project(project_info):

    updated_project = {
        'title' : input('New title: '),
        'details' : input('New details: '),
        'start_time' : input('New start time(DD-MM-YYYY): '),
        'end_time' : input('New end time(DD-MM-YYYY): '),
    }

    if(rewrite_data(project_info[1]) == True):
        if(add_project(updated_project) == True):
                return True
        else:
            add_project(project_info)
            print('Error occured')




def delete_project():
    target_project = input('Project Title: ')
    if(rewrite_data(target_project) == True):
        print('Deleted!✌️')
    else:
        print('Project does not exist')
    display_projects_menu()




def rewrite_data(target_project):
    deleted = False
    with open("projects.txt", "r") as db:
        projects = db.readlines()
    with open("projects.txt", "w") as db:
        for project in projects:
            project_info = project.split(', ')
            project_title = project_info[1]
            project_owner = project_info[0]
            if not (project_owner.lower() == authentication.current_user_email.lower() and project_title.lower() == target_project.lower()):
                db.write(project)
            elif(project_owner.lower() == authentication.current_user_email.lower() and project_title.lower() == target_project.lower()):
                deleted = True

    db.close()
    return deleted




def list_projects():
    projects = open('projects.txt', 'r')
    print(
"""=============
Title : Owner
=============""")
    for project in projects:
        project_info = project.split(', ')
        print(f'{project_info[1]} : {project_info[0]}')

    display_projects_menu()




def search_project():
    p_start_time = input('Enter start time(DD-MM-YYYY): ')
    p_end_time = input('Enter end time(DD-MM-YYYY): ')
    if(project_validation.validate_date(p_start_time) and project_validation.validate_date(p_end_time)):
        formatted_start_date = datetime.strptime(p_start_time, "%d-%m-%Y")
        formatted_end_date = datetime.strptime(p_end_time, "%d-%m-%Y")
        print(
"""=====================================
Title : Owner : Start time : End time
=====================================""")
        projects = open('projects.txt', 'r')
        for project in projects:
            project_info = project.split(', ')
            if(formatted_start_date <= datetime.strptime(project_info[4][0:10], "%d-%m-%Y") and formatted_end_date >= datetime.strptime(project_info[5][0:10], "%d-%m-%Y")):
                print(f'{project_info[1]} : {project_info[0]} : {project_info[4]} : {project_info[5]}')
    else:
        print('Incorrect date format, should be DD-MM-YYYY')
    
    display_projects_menu()




display_projects_menu()