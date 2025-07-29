# register students for an exam venue
# ask the user how many students to register
num_students = int(input("How many students do you want to register? "))
# create a for loop that will run for the number of students
for i in range(num_students):
    # prompt the user to enter the student's name
    name = input(f"Enter the student ID {i + 1}: ")
    # write each of the students ID to a text file called reg_form.txt
    with open('reg_form.txt', 'a') as file:
        file.write(name + "______________" '\n')