# create a random joke generator using built-in functions
import random
# list of jokes
jokes = ["This is a joke about AI. Why did the AI cross the road? To optimize its pathfinding algorithm!",
         "Why did the robot go on a diet? It had too many bytes!", "Why did the computer go to therapy? It had too many unresolved issues!",
         "Why do programmers prefer dark mode? Because light attracts bugs!",]
# function to get a random joke
def get_random_joke():
    return random.choice(jokes)
# print the random joke
if __name__ == "__main__":
    print("Here's a joke for you:")
    print(get_random_joke())