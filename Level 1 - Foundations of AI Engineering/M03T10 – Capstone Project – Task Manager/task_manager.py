import os

# get the path of the current script

current_path = os.path.dirname(os.path.abspath(__file__))
print(f"Current script path: {current_path}")


# Login. Prompt the user to enter a username and password. A list of valid usernames and passwords is stored in the user.txt text file.
# Display an appropriate error message if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password. 
# The user should repeatedly be asked to enter a valid username and password until they provide appropriate credentials.
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
valid_credentials = {}
try:
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


#After a successful login, the user is presented with a menu of options to choose from. The user should be able to repeatedly choose options from the menu until they choose to exit the program. The following menu should be displayed once the user has successfully logged in: "Select one of the following options": r - register a user, a - add task, va - view all tasks, vm - view my tasks, e - exit
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
        "e - exit\n")
        menu = menu.lower()
        if menu in ['r', 'a', 'va', 'vm', 'vc', 'del', 'e']:
            print(f"You selected option: {menu}")
    else:
        menu = input("Select one of the following options:\n"
        "a - add task\n"
        "va - view all tasks\n"
        "vm - view my tasks\n"
        "e - exit\n")
        menu = menu.lower()
        if menu in ['a', 'va', 'vm', 'e']:
            print(f"You selected option: {menu}")

    while menu != 'e':
                #If the user chooses “r” to register a user, they should be prompted for a new username and password. The user should also be asked to confirm the password. If the value entered to confirm the password matches the value of the password, the username and password should be written to user.txt in the appropriate format. if the new user is added the system should return to the menu.

                if menu == 'r' and input_username == 'admin':
                    new_username = input("Enter a new username: ")
                    new_password = input("Enter a new password: ")
                    confirm_password = input("Confirm the new password: ")
                    if new_password == confirm_password:
                        try:
                            with open(file_path, 'a') as user_file:
                                user_file.write(f"{new_username}, {new_password}\n")
                                print("User registered successfully.")
                            break
                        except Exception as e:
                            print(f"An error occurred: {e}")
                    else:
                        print("Passwords do not match. User not registered.")
   
                elif menu == 'a':
                    assigned_to = input("Enter the username of the person the task is assigned to: ")
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
                            break
                    except Exception as e:
                        print(f"An error occurred: {e}") 
                elif menu == 'va':
                    try:
                        with open(file_path1, 'r') as user_file:
                            tasks = user_file.readlines()
                        if not tasks:
                            print("No tasks available.")
                        else:
                            for task in tasks:
                                assigned_to, task_title, task_description, assigned_date, due_date, task_completed = task.strip().split(', ')
                                print(f"Task: {task_title}\nAssigned to: {assigned_to}\nDate Assigned: {assigned_date}\nDue Date: {due_date}\nTask Description: {task_description}\nTask Completed: {task_completed}\n")
                            break 
                    except FileNotFoundError:
                        print("The tasks.txt file was not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                elif menu == 'vm':
                    try:
                        with open(file_path1, 'r') as task_file:
                            tasks = task_file.readlines()
                            user_tasks = [task for task in tasks if task.startswith(input_username + ', ')]
                            if not user_tasks:
                                print("No tasks assigned to you.")
                                break
                            else:
                                for task in user_tasks:
                                    assigned_to, task_title, task_description, assigned_date, due_date, task_completed = task.strip().split(', ')
                                    print(f"Task: {task_title}\nAssigned to: {assigned_to}\nDate Assigned: {assigned_date}\nDue Date: {due_date}\nTask Description: {task_description}\nTask Completed: {task_completed}\n")
                                break
                    except FileNotFoundError:
                        print("The tasks.txt file was not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")

                elif menu == 'vc' and input_username == 'admin':
                    try:
                        with open(file_path1, 'r') as task_file:
                            tasks = task_file.readlines()
                            completed_tasks = [task for task in tasks if task.strip().endswith(', Yes')]
                            if not completed_tasks:
                                print("No completed tasks available.")
                                break
                            else:
                                for task in completed_tasks:
                                    assigned_to, task_title, task_description, assigned_date, due_date, task_completed = task.strip().split(', ')
                                    print(f"Task: {task_title}\nAssigned to: {assigned_to}\nDate Assigned: {assigned_date}\nDue Date: {due_date}\nTask Description: {task_description}\nTask Completed: {task_completed}\n")
                                break
                    except FileNotFoundError:
                        print("The tasks.txt file was not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")

                elif menu == 'del' and input_username == 'admin':
                    try:
                        with open(file_path1, 'r') as task_file:
                            tasks = task_file.readlines()
                        if not tasks:
                            print("No tasks available to delete.")
                            break
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
                                break
                            else:
                                print("Invalid task number.")
                    except FileNotFoundError:
                        print("The tasks.txt file was not found.")
                    except ValueError:
                        print("Please enter a valid number.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
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
                                            
else:
    print("Invalid option. Please try again.")

  