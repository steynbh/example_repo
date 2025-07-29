# open DOB text file and read the contents
with open('DOB.txt', 'r') as file:
    print("Name:")
    # read through each line in the file
    for line in file:
       #print only the names and surnames - the first two words in each line
        parts = line.split()
        if len(parts) >= 2:
            print(parts[0], parts[1])
    # read through each line in the file
with open('DOB.txt', 'r') as file: 
    print("\nBirthdates:")  
    for line in file:
        # print only the dates of birth - the last three words in each line
        parts = line.split()
        if len(parts) >= 3:
            print(parts[-3], parts[-2], parts[-1])  