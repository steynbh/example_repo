import os
from datetime import datetime

# function to register a new user
def reg_user():
    new_username = input("Enter a new username: ")
    # check if the username already exists in user.txt
    try:
        with open(file_path, 'r') as user_file:
            for line in user_file:
                existing_username, _ = line.strip().split(', ')
                existing_username = existing_username.lower()
                if new_username.lower() == existing_username:
                    print("Username already exists. Please choose a different username.")
                    return
        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm the new password: ")
        if new_password == confirm_password:
           try:
                with open(file_path, 'a') as user_file:
                    user_file.write(f"\n{new_username}, {new_password}\n")
                    print("User registered successfully.")
           except Exception as e:
                       print(f"An error occurred: {e}")
        else:
                    print("Passwords do not match. User not registered.")
    except FileNotFoundError:
        print("The user.txt file was not found.")
    return

# function to add a new task
def add_task():
    assigned_to = input("Enter the username of the person the task is assigned to: ")
    # check if the username exists in user.txt
    try:
        with open(file_path, 'r') as user_file:
            usernames = [line.strip().split(', ')[0] for line in user_file]
            usernames = [username.lower() for username in usernames]  # Convert to lowercase for case-insensitive comparison
        if assigned_to.lower() not in usernames:
            print("Username does not exist. Please enter a valid username.")
            return
              
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter a description of the task: ")
        due_date = input("Enter the due date of the task (e.g., 2023-12-31): ")
        from datetime import datetime
        assigned_date = datetime.now().strftime("%Y-%m-%d")
        task_completed = "No"
        try:
            with open(file_path1, 'a') as user_file:
                user_file.write(f"{assigned_to}, {task_title}, {task_description}, {assigned_date}, {due_date}, {task_completed}\n")
                print("Task added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    except FileNotFoundError:
        print("The user.txt file was not found.") 
    return

# function to view all tasks
def view_all():
    list_length = 0
    list_loops = 0
    while list_loops <= list_length:
        try:
            with open(file_path1, 'r') as user_file:
                tasks = user_file.readlines()
                list_length = len(tasks)
                print(f"Total tasks: {list_length}")
                if not tasks:
                    print("No tasks available.")
                    break
                else:
                    for task in tasks:
                            list_loops += 1
                            print(f"Listing task {list_loops} of {list_length}")
                            assigned_to, task_title, task_description, assigned_date, due_date, task_completed = task.strip().split(', ')
                            print(f"Task: {task_title}\nAssigned to: {assigned_to}\nDate Assigned: {assigned_date}\nDue Date: {due_date}\nTask Description: {task_description}\nTask Completed: {task_completed}\n")
                    break
        except FileNotFoundError:
            print("The tasks.txt file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        break
    return

# function to view tasks assigned to the logged-in user    
def view_mine():
    list_length = 0
    list_loops = 0
    while list_loops <= list_length:
        try:
            with open(file_path1, 'r') as task_file:
                tasks = task_file.readlines()
                list_length = len(tasks)
                print(f"Total tasks: {list_length}")
                user_tasks = [task for task in tasks if task.startswith(input_username + ', ')]
                if not user_tasks:
                    print("No tasks assigned to you.")
                    break
                else:
                    for idx, task in enumerate(user_tasks, start=1):
                        list_loops += 1
                        assigned_to, task_title, task_description, assigned_date, due_date, task_completed = task.strip().split(', ')
                        print(f"{idx}. Task: {task_title}, Task description: {task_description}, Assigned date: {assigned_date}, Assigned to: {assigned_to}, Due Date: {due_date}, Completed: {task_completed}")

                #If the user selects a specific task, they should be able to choose to either mark the task as complete or edit the task (i.e., change the username of the person to whom the task is assigned or change the due date of the task).
                print("Options:\n1. Mark a task as complete\n2. Edit a task\n3. Exit")
                option = input("Enter the number of your choice: ")
                if option == '1':
                    task_number = int(input("Enter the number of the task you want to mark as complete: "))
                    if 1 <= task_number <= len(user_tasks):
                        task_to_update = user_tasks[task_number - 1]
                        updated_task = task_to_update.rsplit(', ', 1)[0] + ', Yes\n'
                        tasks[tasks.index(task_to_update)] = updated_task
                        with open(file_path1, 'w') as task_file:
                            task_file.writelines(tasks)
                            print("Task marked as complete.")
                        return False
                    else:
                        print("Invalid task number.")
                elif option == '2':
                    task_number = int(input("Enter the number of the task you want to edit: "))
                    if 1 <= task_number <= len(user_tasks):
                        task_to_edit = user_tasks[task_number - 1]
                        print("Edit Options:\n1. Change assigned user\n2. Change due date")
                        edit_option = input("Enter the number of your choice: ")
                        if edit_option == '1':
                            new_assigned_user = input("Enter the new username to assign the task to: ")
                            parts = task_to_edit.strip().split(', ')
                            parts[0] = new_assigned_user
                            updated_task = ', '.join(parts) + '\n'
                            tasks[tasks.index(task_to_edit)] = updated_task
                            with open(file_path1, 'w') as task_file:
                                task_file.writelines(tasks)
                                print("Task reassigned successfully.")
                            return False
                        elif edit_option == '2':
                            new_due_date = input("Enter the new due date (e.g., 2023-12-31): ")
                            parts = task_to_edit.strip().split(', ')
                            parts[4] = new_due_date
                            updated_task = ', '.join(parts) + '\n'
                            tasks[tasks.index(task_to_edit)] = updated_task
                            with open(file_path1, 'w') as task_file:
                                task_file.writelines(tasks)
                                print("Due date updated successfully.")
                            return False
                        else:
                            print("Invalid edit option.")
                    else:
                        print("Invalid task number.")
                elif option == '3':
                    print("Exiting task management.")
                    return
        except FileNotFoundError:
            print("The tasks.txt file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        break  
    return

# function to view completed tasks    
def view_completed():
    list_length = 0
    list_loops = 0
    while list_loops <= list_length:
        try:
            with open(file_path1, 'r') as task_file:
                tasks = task_file.readlines()
                list_length = len(tasks)
                print(f"Total tasks: {list_length}")
                completed_tasks = [task for task in tasks if task.strip().endswith(', Yes')]
                if not completed_tasks:
                    print("No completed tasks available.")
                    break
                else:
                    for task in completed_tasks:
                        list_loops += 1
                        print(f"Listing completed task {list_loops} of {len(completed_tasks)}")
                        assigned_to, task_title, task_description, assigned_date, due_date, task_completed = task.strip().split(', ')
                        print(f"Task: {task_title}\nAssigned to: {assigned_to}\nDate Assigned: {assigned_date}\nDue Date: {due_date}\nTask Description: {task_description}\nTask Completed: {task_completed}\n")
                    break

        except FileNotFoundError:
            print("The tasks.txt file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        break
    return

# function to delete a task     
def delete_task():
    try:
        with open(file_path1, 'r') as task_file:
            tasks = task_file.readlines()
            if not tasks:
                print("No tasks available to delete.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    assigned_to, task_title, task_description, assigned_date, due_date, task_completed = task.strip().split(', ')
                    print(f"{idx}. Task: {task_title}, Assigned to: {assigned_to}, Due Date: {due_date}, Completed: {task_completed}")
                    
                task_number = int(input("Enter the number of the task you want to delete: "))
                if 1 <= task_number <= len(tasks):
                    del tasks[task_number - 1]
                    with open(file_path1, 'w') as task_file:
                        task_file.writelines(tasks)
                        print("Task deleted successfully.")
                    return False
                else:
                    print("Invalid task number.")
    except FileNotFoundError:
        print("The tasks.txt file was not found.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")    
    return

# function to generate user statistics report
def generate_statistics():
    try:
        with open(file_path, 'r') as user_file:
            users = user_file.readlines()
            total_users = len(users)
            user_list = [user.strip().split(', ')[0] for user in users]
            
    except FileNotFoundError:
        print("The user.txt file was not found.")
        return
# For each user, also describe: 
# 1. The total number of tasks assigned t0o that user. 
# 2. The percentage of the total number of tasks that have been assigned to that user 
# 3. The percentage of the tasks assigned to that user that have been completed 
# 4. The percentage of the tasks assigned to that user that must still be completed 
# 5. The percentage of the tasks assigned to that user that have not yet been completed and are overdue
    try:
        with open(file_path1, 'r') as task_file:
            tasks = task_file.readlines()
            total_tasks = len(tasks)
        with open(file_path3, 'w') as report_file:
            report_file.write(f"Total users registered: {total_users}\n")
            report_file.write(f"Total tasks: {total_tasks}\n\n")
            for user in user_list:
                user_tasks = [task for task in tasks if task.startswith(user + ', ')]
                report_file.write(f"User: {user}\n")
                total_user_tasks = len(user_tasks)
                report_file.write(f"Total tasks assigned: {total_user_tasks}\n")
                percent_total_tasks = (total_user_tasks / total_tasks * 100) if total_tasks > 0 else 0
                report_file.write(f"Percentage of total tasks assigned: {percent_total_tasks:.2f}%\n")
                completed_user_tasks = sum(1 for task in user_tasks if task.strip().endswith(', Yes'))
                percent_completed = (completed_user_tasks / total_user_tasks * 100) if total_user_tasks > 0 else 0
                report_file.write(f"Percentage of tasks completed: {percent_completed:.2f}%\n")
                incomplete_user_tasks = total_user_tasks - completed_user_tasks
                percent_incomplete = (incomplete_user_tasks / total_user_tasks * 100) if total_user_tasks > 0 else 0
                report_file.write(f"Percentage of tasks to be completed: {percent_incomplete:.2f}%\n")
                from datetime import datetime
                overdue_user_tasks = sum(1 for task in user_tasks if not task.strip().endswith(', Yes') and datetime.strptime(task.strip().split(', ')[4], "%Y-%m-%d") < datetime.now())
                percent_overdue = (overdue_user_tasks / total_user_tasks * 100) if total_user_tasks > 0 else 0
                report_file.write(f"Percentage of tasks overdue: {percent_overdue:.2f}%\n\n")
                           
        print("User statistics displayed successfully.")
    except FileNotFoundError:
        print("The tasks.txt file was not found.")
    except FileNotFoundError:
        print("The user.txt file was not found.")

# function to display user statistics report    
def display_statistics():
    try:
        with open(file_path3, 'r') as report_file:
            statistics = report_file.read()
            print(statistics)
    except FileNotFoundError:
        print("The user_overview.txt file was not found. Please generate the reports first.")

# function to generate task report
def generate_task_report():
    try:
        with open(file_path1, 'r') as task_file:
            tasks = task_file.readlines()
            total_tasks = len(tasks)
            completed_tasks = sum(1 for task in tasks if task.strip().endswith(', Yes'))
            incomplete_tasks = total_tasks - completed_tasks
            overdue_tasks = sum(1 for task in tasks if not task.strip().endswith(', Yes') and datetime.strptime(task.strip().split(', ')[4], "%Y-%m-%d") < datetime.now())
            percent_incomplete = (incomplete_tasks / total_tasks * 100) if total_tasks > 0 else 0
            percent_overdue = (overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0
        with open(file_path2, 'w') as report_file:
            report_file.write(f"Total tasks: {total_tasks}\n")
            report_file.write(f"Completed tasks: {completed_tasks}\n")
            report_file.write(f"Incomplete tasks: {incomplete_tasks}\n")
            report_file.write(f"Overdue tasks: {overdue_tasks}\n")
            report_file.write(f"Percentage of incomplete tasks: {percent_incomplete:.2f}%\n")
            report_file.write(f"Percentage of overdue tasks: {percent_overdue:.2f}%\n")
            print("Task report generated successfully.")
    except FileNotFoundError:
        print("The tasks.txt file was not found.")

# function to display task report
def display_task_report():
    try:
        with open(file_path2, 'r') as report_file:
            report = report_file.read()
            print(report)
    except FileNotFoundError:
        print("The task_overview.txt file was not found. Please generate the reports first.")
    
# Login. Prompt the user to enter a username and password. 
# A list of valid usernames and passwords is stored in the user.txt text file.
# Display an appropriate error message if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password. 
# The user should repeatedly be asked to enter a valid username and password until they provide appropriate credentials.
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
valid_credentials = {}
try:
    script_dir2 = os.path.dirname(__file__)  # Get the directory of the current script
    file_path2 = os.path.join(script_dir2, 'task_overview.txt')
    script_dir3 = os.path.dirname(__file__)  # Get the directory of the current script
    file_path3 = os.path.join(script_dir3, 'user_overview.txt')
    script_dir1 = os.path.dirname(__file__)  # Get the directory of the current script
    file_path1 = os.path.join(script_dir1, 'tasks.txt')
    script_dir = os.path.dirname(__file__)  # Get the directory of the current script
    file_path = os.path.join(script_dir, 'user.txt')
    with open(file_path, 'r') as user_file:
        for line in user_file:
            username, password = line.strip().split(', ')
            valid_credentials[username] = password
except FileNotFoundError:
    print("The user.txt file was not found.")
    exit()
while True:
    if input_username in valid_credentials:
        if input_password == valid_credentials[input_username]:
            print("Login successful.")
            break
        else:
            print("Invalid password. Please try again.")
    else:
        print("Invalid username. Please try again.")
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")
# if username is admin, show the admin menu. Otherwise, show the user menu.
# The admin user should be able to register a new user, add a task, view all tasks, view their own tasks, view completed tasks, delete tasks or exit the program.
if input_username == 'admin':
    print("Welcome, admin! You have access to the admin menu.")
else:
    print(f"Welcome, {input_username}! You have access to the user menu.")

#After a successful login, the user is presented with a menu of options to choose from. 
# The user should be able to repeatedly choose options from the menu until they choose to exit the program. 
# The following menu should be displayed once the user has successfully logged in: "Select one of the following options": r - register a user, a - add task, va - view all tasks, vm - view my tasks, e - exit
# The user should be able to choose an option by entering the letter associated with the relevant option in the menu. The program should respond appropriately to the user's menu selection.
# The program should be case insensitive to the user's menu selection. For example, if the user enters 'A' or 'a', the program should respond appropriately to the user's menu selection.
# If the user enters any letter other than the letters specified in the menu, an appropriate error message should be displayed.
# The program should then re-display the menu and prompt the user to make another selection.
# The program should only exit when the user selects the 'e' option from the menu.
# The program should respond appropriately to the user's menu selection as follows:
while True:
    if input_username == 'admin':
        menu = input("Select one of the following options:\n"
        "r - register a user\n"
        "a - add task\n"
        "va - view all tasks\n"
        "vm - view my tasks\n"
        "vc - view completed tasks\n"
        "del - delete task\n"
        "gs - display statistics\n"
        "gr - generate reports\n"
        "e - exit\n")
        menu = menu.lower()
        if menu in ['r', 'a', 'va', 'vm', 'vc', 'del', 'e']:
            print(f"You selected option: {menu}")
        
    elif input_username != 'admin':
        menu = input("Select one of the following options:\n"
        "a - add task\n"
        "va - view all tasks\n"
        "vm - view my tasks\n"
        "e - exit\n")
        menu = menu.lower()
        if menu in ['a', 'va', 'vm', 'e']:
            print(f"You selected option: {menu}")
        

    while menu != 'e':
                
                if menu == 'r' and input_username == 'admin':
                    reg_user()
                    break
                    
                elif menu == 'a':
                    add_task()
                    break
                    
                elif menu == 'va':
                    view_all()
                    break
                        
                elif menu == 'vm':
                    view_mine()
                    break
                                                        
                elif menu == 'vc' and input_username == 'admin':
                    view_completed()
                    break

                elif menu == 'del' and input_username == 'admin':
                    delete_task()
                    break
                            
                elif menu == 'gs' and input_username == 'admin':
                    generate_statistics()
                    display_statistics()
                    break

                elif menu == 'gr' and input_username == 'admin':
                    from datetime import datetime
                    generate_task_report()
                    display_task_report()
                    break

                else: 
                    print("Invalid option. Please try again.")
                    break


    if menu == 'e':
                # do you want to login as another user?
                input_exit = input("Do you want to login as another user? (yes/no): ").lower()
                while True:
                    if input_exit == 'yes':
                        input_username = input("Enter your username: ")
                        input_password = input("Enter your password: ")
                        while True:
                            if input_username in valid_credentials:
                                if input_password == valid_credentials[input_username]:
                                    print("Login successful.")
                                    break
                                else:
                                    print("Invalid password. Please try again.")
                            else:
                                print("Invalid username. Please try again.")
                            input_username = input("Enter your username: ")
                            input_password = input("Enter your password: ")
                    elif input_exit == 'no':
                        print("Exiting the program.")
                        exit()
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        input_exit = input("Do you want to login as another user? (yes/no): ").lower()
                    break
                # end of program