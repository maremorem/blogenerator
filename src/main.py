import re
import sys
from typing import List

helpmessage = '''Available commands:
help -> shows this message
quit -> exit blogenerator
'''

# Reusable user input loop.
    # You can specify a list of fixed outcomes or a regex pattern to check against
def userinput(message: str, choices: List[str]=[], pattern: str=""):
    print(message)
    value = input()
    while True:
        if value in choices:
            return value
        else:
            if pattern != "" and re.match(pattern, value):
                return value
            elif value == "help":
                print(helpmessage)
                input("Press enter to continue:")
                print(message)
            elif value == "quit":
                sys.exit()
            else:
                print("Invalid input. Please try again.")
                print(message)
            value = input()

# choice = userinput("EXAMPLE Please enter a value of a, b, or c. OR enter a filename ending with .md:", ["a", "b", "c"], r".*\.md$")
# print(f"Returned value: {choice}")

print("Welcome to Blogenerator v0.1!")
filename = userinput("Please enter the name of your new blog post. Format: <filename.md>", [], r".*\.md$")
try:
   blogfile = open(filename)
except:
    print("File failed to open. Exiting..")
    sys.exit()

print(f"Successfully loaded {filename} for conversion.")
# print("Current template file: template.html\n   -> Do you want to choose a new template file? (y/n)")
# # another input chooser goes here
# input()
# print("Initialising..") 
