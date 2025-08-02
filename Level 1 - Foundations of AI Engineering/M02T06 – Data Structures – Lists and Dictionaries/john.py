#while string is not "John" enter string into list
incorrect_list = []
string_item = 0
while string_item != "John":
    #make sure that uppercase and lowercase are not considered different
    string_item = input("Enter your name : ").strip().capitalize()
    incorrect_list.append(string_item)
    # do not print "John" in the list
    if string_item == "John":
        incorrect_list.pop()
print("List of incorrect names:", incorrect_list)