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
            print("choices match!")
            return value
        else:
            if pattern != "" and re.match(pattern, value):
                print("re match!")
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

print("Welcome to Blogenerator v0.1!\nPlease enter your new blog post. Format: <filename.md>")






# while True: #need to fix this loop still. It doesn't let you ctrl+c or quit.
#     try:
#         blogfile = input()

#         if blogfile == "help":
#             print(helpmessage)
#             pass
#         elif blogfile == "quit":
#             sys.exit() # why doesn't this work??
#         else:
#             pass

#         pattern = r".*\.md$" # Pattern: A string STARTING with any character (.*) and ENDING in the literal .md (\.md$)
#         if re.match(pattern, blogfile):
#             break 
#         else:
#             raise TypeError("Incorrect format")
#     except:
#         print("Please try again! Format: <filename>.md")

# print(f"Successfully loaded {blogfile} for conversion.")
# print("Current template file: template.html\n   -> Do you want to choose a new template file? (y/n)")
# # another input chooser goes here
# input()
# print("Initialising..") 
