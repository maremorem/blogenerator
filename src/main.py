import re
import sys
from typing import List

helpmessage = '''Available commands:
help -> shows this message
quit -> exit blogenerator
'''

# Reusable user input loop.
    # You can specify a list of fixed outcomes or a regex pattern to check against
def userinput(message: str, choices: List[str]=[], pattern: str="", example: str=None):
    if pattern != "" and example == None:
        raise RuntimeError("You specified a regex pattern in userinput but forgot to supply an example!")
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
                print("Invalid input. ")
                if choices != [] and pattern == "": # when only using choices
                    print("Options: ", end="")
                    print("(", end="")
                    for i in choices[:-1]:
                        print(i, end="/")
                    print(f"{choices[-1]})")
                elif pattern != "" and choices == []: # when only using pattern
                    print(f"Example: {example}")
                else: # when choices and pattern are both defined. Very unlikely case
                    print("Options: ", end="")
                    print("(", end="")
                    for i in choices[:-1]:
                        print(i, end="/")
                    print(f"{choices[-1]}),\nor something in the format: {example}")

            value = input()

# choice = userinput("EXAMPLE Please enter a value of a, b, or c. OR enter a filename ending with .md:", ["a", "b", "c"], r".*\.md$", "samplexample.md")
# print(f"Returned value: {choice}")

print("Welcome to Blogenerator v0.1!")
filename = userinput("Please enter the name of your new blog post. Example: <filename.md>", [], r".*\.md$", "mycoolblog.md")
try:
    blogfile = open(filename)
except:
    print("File failed to open. Exiting..")
    sys.exit()
print(f"Successfully loaded {filename} for conversion.")

print("The current template file is template.html")
choice = userinput("   -> Do you want to choose a different template file? (y/n)", ["y", "n"])
if choice == "y":
    # user goes on to choose their template file. 
    # (Turn the previous file chooser into a function and use here)
    pass
else:
    # run file chooser and load default template file
    pass
print("Initialising..") 
