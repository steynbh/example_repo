# define a function to print dictionary values if given the key
def print_value(dictionary, key):
    for k, v in dictionary.items():
        if k == key:
            print(v)
            return  
    
# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", 
                         "maggie": "(Pacifier Suck)"
                         }

# Print dictionary values from simpson_catch_phrases

print_value(simpson_catch_phrases, "lisa")
