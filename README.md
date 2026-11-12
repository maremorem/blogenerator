# Blogenerator
Welcome to my repo.
The purpose of this project is to dynamically add blog posts to my static website.

## Usage
1. Write your blog post in a markdown file.
It should contain the following front matter properties:
- title
- description
- created
- lastmod\* (optional)
- tags
- cover (path to an image)
- lang

Creation and modification dates must be specified in ISO format. For example:
`2026-11-20T01:20:00`
- The timestamp variable is currently set to Sydney Australia. This means that the offset for the current time of year in Sydney will be appended to the above datetime to comply with ISO 8601, which is required for opengraph meta creation info.

2. Alter the template file however you would like to style it. Frontmatter data is inserted into any block like this: `{{%%block%%}}`
- In the above case, any front matter value matching a property of "block" will be inserted in.
3. Run main.py in the same directory as your blog file. Follow the interactive instructions.
4. It will build an html output to `/blog/`.
5. Rejoice
