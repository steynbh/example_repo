# open DOB text file and read the contents
import os
print (os.path.dirname(__file__))
with open('DOB.txt', 'r') as file:
    # read through each line in the file
    for line in file:
       print (line)
       