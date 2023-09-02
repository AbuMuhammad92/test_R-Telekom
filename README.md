# Web Service for Dynamically Sorting Dictionaries

This project represents a web service created using FastAPI for dynamically sorting dictionaries.

## Prerequisites

- Python 3.6 or newer.
- Installed Pip.

## Installation and Setup

1. Install the required libraries:
   pip install fastapi[all] uvicorn

2. Run the server using the following command:
   uvicorn main:app --reload

3. Open a web browser and navigate to:
   http://127.0.0.1:8000/html/
  

Project Files
main.py: The main file containing routes for the web application.
myname.py: The file containing the function for processing data, which can be dynamically imported.
templates/functions.html: An HTML template used to display a list of available functions and their code on a web page.



