# Content Tracker App

## Dependencies

* flask
* flask-wtf
* flask_sqlalchemy
* bootstrap (CDN)
* sqlite3 (in-memory)

## Description

#### Purpose
This is a small web application developed as a term project for the course MET CS 521 at Boston University. The app is built entirely using Python and the Flask microframework to showcase the usage of Python structures and MVC concepts.

#### Usage
The application will track the lifecycle of product-related content, such as media files, documents, etc. It should display in the UI when the content expires, which the user can specify via a form. Visual cues indicate when content needs updating soon. Version details and owner email are attached to each piece of content.

#### Roadmap
Possible features in the future include:
* Owner notifications via email 7 days before content expiration date
* Upload/Download of file attachments
* Authentication with JSON Web Tokens