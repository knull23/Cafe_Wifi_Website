# Cafe Finder Project

## Description
The Cafe Finder app is a simple Flask-based web application that allows users to view, add, and delete cafes. Each cafe entry includes important details such as name, location, opening and closing times, and ratings for coffee, WiFi, and power availability. The project demonstrates the use of Flask, SQLAlchemy for database management, Flask-WTF for form handling, and Bootstrap for a responsive design.

## Features
- **View All Cafes:** A home page that lists all cafes stored in the database with key information.
- **Add New Cafe:** A form to add a new cafe to the database, including details like name, location, and ratings.
- **Delete Cafe:** The ability to delete a cafe entry from the database.
- **Responsive Design:** The app is designed to be responsive and works well on different screen sizes, thanks to the integration of Bootstrap 5.

## Technologies Used
- **Flask** - Web framework for building the application.
- **SQLAlchemy** - ORM for managing the SQLite database.
- **Flask-WTF** - For form handling and validation.
- **Bootstrap 5** - Front-end framework for a responsive design.
- **SQLite** - Database for storing cafe information.
- **Jinja2** - Templating engine for rendering HTML.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Steps
  Clone the repository:
  git clone https://github.com/your-username/cafe-finder.git
  
  Navigate into the project folder:
  cd cafe-finder
  
  Create a virtual environment:
  python -m venv venv
  
  Activate the virtual environment:
  For Windows: venv\Scripts\activate
  For Mac/Linux: source venv/bin/activate
  
  Install the required dependencies:
  pip install -r requirements.txt
  
  Create the SQLite database:
  python main.py
  
  Run the application:
  flask run
  
  Access the app by opening http://127.0.0.1:5000/ in your browser.
  
  Make sure to replace your-username with your actual GitHub username when cloning the repository.

## Project Structure
  cafe-finder/
  │
  ├── main.py            # Main application file with routes
  ├── models.py          # Database models
  ├── forms.py           # Forms used for adding cafes
  ├── templates/         # HTML templates (index.html, add.html, cafes.html)
  │   ├── index.html
  │   ├── add.html
  │   ├── cafes.html
  ├── static/            # Static files (CSS, JS, Images)
  │
  └── requirements.txt   # Python dependencies
