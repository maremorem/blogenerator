import datetime
import re
import sys
from typing import List
import yaml


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

def loadfile(loadfilename):
    try:
        with open(loadfilename, "r") as loadedfile:
            return loadedfile.read()
    except:
        print("Failed to load file; check it exists.")

# LOAD THE BLOG FILE AND TEMPLATE FILE
print("Welcome to Blogenerator v0.1!")
# filename = userinput("Please enter the name of your new blog post. Example: <filename.md>", [], r".*\.md$", "mycoolblog.md")
filename = "blogtest.md"
try:
    with open(filename, "r") as loaded:
        blogfile = loaded.read()
except:
    print("File failed to open. Exiting..") # like in the subsequent comment, make a way to integrate a loop directly into the function in case of errors
    sys.exit()

print(f"Successfully loaded {filename} for conversion.\n\n=====CONTENT BEGIN=====\n{blogfile}\n=====CONTENT END=====\n")

print("The current template file is template.html")
# choice = userinput("   -> Do you want to choose a different template file? (y/n)", ["y", "n"])
choice = "n"

if choice == "y":
    templatefile = None
    while templatefile == None: # figure out a way to integrate this loop into the actual function
        templatefile = loadfile(userinput("Please enter the name of your html template.", [], r".*\.html$", "example.html"))
else:
    templatefile = loadfile("template.html")


print("Initialising..") 
frontmatter = str()

# MAIN FUNCTIONALITY

# Get frontmatter metadata
blogfilelist = blogfile.splitlines()
if blogfilelist[0] == "---":
    count = 0
    for i in blogfilelist:
        if count == 1:
            frontmatter = i
        elif count > 1 and i != "---":
            frontmatter = frontmatter + "\n" + i
        elif i == "---" and count > 0:
            break
        count = count + 1
        
    # turn it into a dictionary
    metadata = yaml.safe_load(frontmatter)
else:
    raise RuntimeError("Missing blog metadata")


print(f"Metadata: {metadata}")

# PARSE AND SUBSTITE ALL THE METADATA THINGIES BASED ON FRONTMATTER ENTRIES
result = templatefile
for key, value in metadata.items():
    # print(key, value)
    if key == "tags":
        print(value)
        for tag in value:
            pattern = r"\{\{%%tags%%\}\}"
            metapattern = r"\{\{%%metatags%%\}\}"
            if tag != value[-1]: 
                result = re.sub(pattern, "<li>"+tag+"</li>{{%%tags%%}}", result) # sub into html body
                result = re.sub(metapattern, "<meta property=\"article:tag\" content=\""+tag+"\">\n    {{%%metatags%%}}", result) # sub into meta tags

            else: 
                result = re.sub(pattern, f"<li>{tag}</li>", result) # for the last tag
                result = re.sub(metapattern, "<meta property=\"article:tag\" content=\""+tag+"\">", result) # last metatag
    else:
        pattern = r"\{\{%%" + re.escape(key) + r"%%\}\}"
        result = re.sub(pattern, lambda m, v=value: str(v), result)

print(result)