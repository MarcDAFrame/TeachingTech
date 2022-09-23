# Week 3: Introduction to HTML

https://www.w3schools.com/html/html_intro.asp
## What is HTML
- HTML stands for Hyper Text Markup Language
- A markup language is distinct from a programming language 
    - typically have little to no logic
    - are purely used to define how something should look or appear to an end user
- other markup languages include 
    - Markdown: the language that these lessons are written in 
    - XML: typically used for configuration files, it was the basis of HTML

## Example of HTML
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
    </body>
</html>
```

- The` <!DOCTYPE html>` declaration defines that this document is an HTML5 document
- The `<html>` element is the root element of an HTML page
- The `<head>` element contains meta information about the HTML page
- The `<title>` element specifies a title for the HTML page (which is shown in the browser's title bar or in the page's tab)
- The `<body>` element defines the document's body, and is a container for all the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.
- The `<h1>` element defines a large heading
- The `<p>` element defines a paragraph


## What is an HTML Element
- an HTML tag is comprised of a few things
    - start tag
    - children (content)
    - end tag
- some HTML tags are self closing
    - line break tag: `<br />`
    - don't have children


## HTML History
| Year | Version |
| --- | --- |
| 1989 | Tim Berners-Lee invented www |
| 1991 | Tim Berners-Lee invented HTML |
| 1993 | Dave Raggett drafted HTML+ |
| 1995 | HTML Working Group defined HTML 2.0 |
| 1997 | W3C Recommendation: HTML 3.2 |
| 1999 | W3C Recommendation: HTML 4.01 |
| 2000 | W3C Recommendation: XHTML 1.0 |
| 2008 | WHATWG HTML5 First Public Draft |
| 2012 | WHATWG HTML5 Living Standard |
| 2014 | W3C Recommendation: HTML5 |
| 2016 | W3C Candidate Recommendation: HTML 5.1 |
| 2017 | W3C Recommendation: HTML5.1 2nd Edition |
| 2017 | W3C Recommendation: HTML5.2 |





# Thoughts
- different tags
  - img
  - div
  - section
  - h1, h2 ... 
  - canvas
  - style
  - script
- tag attributes
- position system
  - https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning
- display system
  - 