import re
import sys

helpmessage = '''Available commands:
help -> shows this message
quit -> exit blogenerator
'''

print("Welcome to Blogenerator v0.1!\nPlease enter your new blog post. Format: <filename.md>")


while True: #need to fix this loop still. It doesn't let you ctrl+c or quit.
    try:
        blogfile = input()

        if blogfile == "help":
            print(helpmessage)
            pass
        elif blogfile == "quit":
            sys.exit() # why doesn't this work??
        else:
            pass

        pattern = r".*\.md$" # Pattern: A string STARTING with any character (.*) and ENDING in the literal .md (\.md$)
        if re.match(pattern, blogfile):
            break 
        else:
            raise TypeError("Incorrect format")
    except:
        print("Please try again! Format: <filename>.md")

print(f"Successfully loaded {blogfile} for conversion.")
print("Current template file: template.html\n   -> Do you want to choose a new template file? (y/n)")
# another input chooser goes here
input()
print("Initialising..") 
