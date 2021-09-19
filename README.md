### Python / Django CSV Download and import to DB

A customer would like to have a native mobile application that displays a simple data set, coming from a
spreadsheet. This document can be updated anytime by the client itself, so our API has to be resilient.
The data consists of:
Image
Title
Description (optional)
The spreadsheet is accessible as a CSV file through the following link: https://docs.google.com/spreadsheet/ccc?key=0Aqg9JQbnOwBwdEZFN2JKeldGZGFzUWVrNDBsczZxLUE&single=true&gid=0&output=csv

### The Task

Because the CSV could potentially be moved to another location, replaced by another one or it could be
temporally unavailable an API should be implemented in between. Build a RESTful JSON API in Django t
hat will be used by the mobile application to fetch the CSV contents.
Things to take into consideration:
The CSV and its contents are not reliable.
The CSV could grow very big in size.
The frontend, at least, has to be able to get the list of entries and the details of a single one.
Include clear instructions on how to run it.
Include unit tests.
Bonus points:
Have a dockerized setup.
Think of this as a real project that will go to production.
A good cache strategy.
