# prompt the userto enter a sentence
user_input = input("Please enter a sentence: ")
# convert every alternate letter to uppercase and every other to lowercase
modified_input = ''.join(user_input[i].upper() if i % 2 == 0 else user_input[i].lower() for i in range(len(user_input)))
# print the modified sentence
print("Modified sentence:", modified_input)
# prompt the user to enter a sentence
user_input = input("Please enter another sentence: ")
# convert every alternate word to uppercase and every other to lowercase
modified_input = ' '.join(word.lower() if i % 2 == 0 else word.upper() for i, word in enumerate(user_input.split()))
# print the modified sentence
print("Modified sentence:", modified_input)