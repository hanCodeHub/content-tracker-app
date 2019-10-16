# Content Tracker App

## Dependencies

* flask
* flask-wtf
* flask-sqlalchemy
* bootstrap (CDN)
* sqlite3 (in-memory)

## Description

#### Intro
This is a small web application developed as a term project for the course MET CS 521 at Boston University. The web app is built entirely using Python and the Flask microframework to showcase the usage of Python functional and OOP programming, relational databases, and Model-View-Controller concepts. Some Javascript (ES6) is used to handle events and asynchronous requests within Jinja2 templates.

#### Purpose
Content creators, such as designers, developers, or writers face a similar problem: it's hard to track the who, the what and the when of updates. The application will track the lifecycle of product-related content, such as media files, documents, videos, etc. It does so by allowing users to create content owners responsible for updating content, and then assigning content to them. The app will then show the specified number of days left before a piece of content needs updating, and who's responsible for it.

#### Usage
Users can create or delete (content) owners on the owners page. Here, users must specify an owner's name and email via a validated form. All owners are listed in a table, which also shows on which date each owner was created.

Users can create, edit or delete content on the user page. Here, users can specify the content name and type of the content, as well as how many months it is valid for until the next update. The user then assigns an owner to that content, so that the right person may be contacted to update it when the content expires. At any point, users may change the content information, including its assigned owner, upon which the expiry date resets.

#### Roadmap
Possible features in the future include:
* Automated owner notifications via email 7 days before content expiration date
* Upload/Download of file attachments
* Authentication with JSON Web Tokens