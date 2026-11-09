# Blogenerator
Welcome to my repo.
The purpose of this project is to dynamically add blog posts to my static website.
I'm first going to implement this in python, and then once I get more familiar with rust, I will redo it in rust.

## Usage

Creation and modification dates must be specified in ISO format. For example:
`2026-11-20T01:20:00`
- The timestamp variable is currently set to Sydney Australia. This means that the offset for the current time of year in Sydney will be appended to the above datetime to comply with ISO 8601, which is required for opengraph meta creation info.

Your blog post should contain the following properties:
- title
- description
- created
- lastmod\*
- tags
- cover (path to an image)
- lang



**Blogenerator will work like this:**

1. I write a blog article in markdown.
2. Script reads the markdown file and converts it to html depending on a specified html template file I made (start off hardcoded, then I can make this dynamic)
3. Script updates a 'master' blog page containing all blog posts with a link and preview to the new blog article.

---

It will run on a command line interface on both windows and linux.


## Requirements
md posts can contain front matter attributes that show up on the final page. These include:
- date written
- 

All generated posts are to be hidden from AI crawlers, and google search results where possible. There will be defences in place to block crawlers that misbehave.
    RATIONALE: The contents of some of my blog posts might be personal stories that I want to share with my fans, but keep out of direct data harvesting as much as possible.
- robots.txt will disallow the /blog directory
- all blog post pages contain the noindex attribute by default. This can be optionally disabled in the script's dialog.
- I will enable the 'AI labyrinth' setting in cloudflare



## Future Features
- Japanese localisation

# Notes to self 
## Todo
- [ ] Understand how fonts work in tailwind, and load them locally/in the most efficient way
- [ ] Finish the blog template. Use obsidian templater syntax as inspiration
- [ ] Implement the blogenerator functionality in main.py

## Useful things
https://regex101.com/


https://developer.mozilla.org/en-US/docs/Web/API/Web_components
https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots

Don't repeat yourself:
https://dev.to/anuradha9712/create-reusable-web-components-in-html-1llc
