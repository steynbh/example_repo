class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)


    #Method to print the head office location as Cape Town
    def head_office(self):
        print("The head office is located in Cape Town.")

    # create a subclass of the course class named OOPCourse
class OOPCourse(Course):
    # Class attribute for the course name
    name = "Object-Oriented Programming"

    # create a constructor that initializes the following attributes:
    # discription = "OOP fundamentals", trainer = "Mr Anon A. Mouse"
    def __init__(self, description = "OOP fundamentals", trainer = "Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer
    # create a method that prints the course description and trainer
    def trainer_details(self):
        print(f"Course Description: {self.description}")
        print(f"Trainer: {self.trainer}")

    # create a method in the subcourse subclass called show_course_id that prints the id number of the course #12345
    def show_course_id(self):
        print("Course ID: 12345")

# create an object in the subclass OOPCourse called course_1 and call the methods contact_details, trainer_details and show_course_id
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
       
# Example usage:
# Create an instance of the Course class
course = Course()


# Call the head_office method to display the head office location
course.head_office()
