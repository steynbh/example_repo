import sqlite3


# Creates or opens a file called student_db with an SQLite3 DB 
db = sqlite3.connect("python_programming_db.db")

cursor = db.cursor()  # Get a cursor object 

# Execute a SQL command to create the student table 
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS python_programming( 
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        grade INTEGER 
    ) 
''') 
# Commit the changes to the database to ensure they are saved 
db.commit()


# Insert multiple records into the table using a list of tuples
students_grades = [(55, "Carl Davis", 61), (66, "Dennis Fredrickson", 88), (77, "Jane Richards", 78), (12, "Peyton Sawyer", 45), (2, "Lucas Brooke", 99)] 
 
cursor.executemany( 
    '''INSERT INTO python_programming(id, name, grade) VALUES(?, ?, ?)''', students_grades 
) 

# print the table contents
print("Initial table contents:")
cursor.execute('''SELECT * FROM python_programming''')
contents = cursor.fetchall()  # Fetch all results from the executed SQL command
for content in contents:
    print(content)  # Print each record
    


db.commit()

# Select all records with a grade between 60 and 80
print("\nRecords with grades between 60 and 80:")
cursor.execute('''SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80''')
records = cursor.fetchall()  # Fetch all results from the executed SQL command
for record in records:
    print(record)  # Print each record

# Change Carl Davis’s grade to 65.
print("\nUpdating Carl Davis's grade to 65:")
cursor.execute('''UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis' ''')
# print the updated table contents
cursor.execute('''SELECT * FROM python_programming''')
contents = cursor.fetchall()  # Fetch all results from the executed SQL command
for content in contents:
    print(content)  # Print each record

db.commit()

# Delete Dennis Fredrickson’s row from the table.
print("\nDeleting Dennis Fredrickson's record:")
cursor.execute('''DELETE FROM python_programming WHERE name = 'Dennis Fredrickson' ''')
# print the updated table contents
cursor.execute('''SELECT * FROM python_programming''')
contents = cursor.fetchall()  # Fetch all results from the executed SQL command
for content in contents:
    print(content)  # Print each record

db.commit() 

# Change the grade of all students with an id greater than 55 to 80.
print("\nUpdating grades of students with id greater than 55 to 80:")
cursor.execute('''UPDATE python_programming SET grade = 80 WHERE id > 55 ''')
# print the updated table contents
cursor.execute('''SELECT * FROM python_programming''')
contents = cursor.fetchall()  # Fetch all results from the executed SQL command
for content in contents:
    print(content)  # Print each record
    print()
db.commit()

# Close the database connection
db.close()

