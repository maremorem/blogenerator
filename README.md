# Blogenerator
Welcome to my repo.
The purpose of this project is to dynamically add blog posts to my static website.
I'm first going to implement this in python, and then once I get more familiar with rust, I will redo it in rust.


Blogenerator will work like this:

1. I write a blog article in markdown.
2. Script reads the markdown file and converts it to html depending on a specified html template file I made (start off hardcoded, then I can make this dynamic)
3. Script updates a 'master' blog page containing all blog posts with a link and preview to the new blog article.

---

## Requirements
md posts can contain front matter attributes that show up on the final page. These include:
- date written
- 

All generated posts are to be hidden from AI crawlers, and google search results where possible. There will be defences in place to block crawlers that misbehave.
    RATIONALE: The contents of some of my blog posts might be personal stories that I want to share with my fans, but keep out of direct data harvesting as much as possible.
- robots.txt will disallow the /blog directory
- all blog post pages contain the noindex attribute
- 