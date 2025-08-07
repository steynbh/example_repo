"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object
# create the class, constructor and methods to create a new Email object.
class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address # Initialise the instance variables for each email.
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False # Create the 'mark_as_read()' method to change the 'has_been_read'

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.

    def mark_as_read(self):
        self.has_been_read = True
    pass   

# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    # Create an email object with the email address, subject line and content and store it in the inbox list.
    inbox.append(Email("John@HyperionDev", "Welcome to HyperionDev!", "This is your first email."))
    inbox.append(Email("Mary@HyperionDev", "Great work on the Bootcamp!", "Keep it up!"))
    inbox.append(Email("Peter@HyperionDev", "Your excellent marks!", "Well done!"))
pass

def list_emails():
    # Create a function that prints each email's subject line alongside its corresponding index number, regardless of whether the email has been read.
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line} {'(Read)' if email.has_been_read else '(Unread)'}")
pass

def read_email(index):
    # Create a function that displays the email_address, subject_line and email_content attributes for the selected email.
    if index < len(inbox):
       email = inbox[index]
       print(f"From: {email.email_address}")
       print(f"Subject: {email.subject_line}")
       print(f"Content: {email.email_content}")
        # After displaying these details, use the 'mark_as_read()' method
        # to set its 'has_been_read' instance variable to True.
       email.mark_as_read()
       print(f"\nEmail from {email.email_address} has been marked as read.\n")   
        # After displaying these details, use the 'mark_as_read()' method to set its 'has_been_read' instance variable to True.
               
    else:
        print("Invalid email index.")
#pass


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines along with their corresponding index numbers.
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line} (Unread)")
pass
    # The list of displayed emails should update as emails are read.
    

# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox = []

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()


# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
# Display the menu options for each iteration of the loop.
print("Welcome to the Email Simulator!")
print("Your current inbox contains the following emails:")
list_emails()

while True:
    print("You have the following options:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    print("Please select an option by entering the corresponding number.")

    user_choice = int(
        input(    )
    )

    """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """

    if user_choice == 1:
        # Add logic here to read an email
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
                    
    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()
        
    elif user_choice == 3:
        # Add logic here to quit application.
        print("Thank you for using the Email Simulator. Goodbye!")
        break
    # If the user enters an invalid option, display an error message.
    else:
        print("Oops - incorrect input.")
