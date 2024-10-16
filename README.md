**The Show**

The Show project is a Flask API for managing and viewing episodes and guests of a fictional TV show. It includes endpoints to create, retrieve, and manage episodes, guests, and appearances on the show. The project uses SQLAlchemy for ORM and SQLite for data storage.

**Table of Contents**

***Features**

1. Project Structure
2. Getting Started
3. Installation
4. Database Setup and Seeding
5. Running the Application


6. API Endpoints

    1. GET /episodes
    2. GET /episodes/
    3. GET /guests
    4. POST /appearances

7. Models
8. License


**Features**

    i. RESTful API for managing episodes, guests, and appearances.
    ii. Data validation and error handling.
    iii. Seed data from a CSV file.
    iv. Cascade deletion of related records.
    v. JSON responses with nested data for relationships.


**Project Structure**


the_show/

├── app.py               # Main Flask application file with routes
├── config.py            # Application configuration
├── models.py            # SQLAlchemy models for the project
├── seed.py              # Script for seeding the database
├── the_show.csv         # Sample CSV file for seeding data
└── migrations/          # Migration folder created by Flask-Migrate


**Installation**

1. Clone the repository:


git clone git@github.com:Donrioo90/the_show.git

cd the_show

2. Set up a virtual environment:

pipenv install flask flask_sqlalchemy flask_migrate

pipenv shell

3. Install the dependencies:


pipenv install flask flask_sqlalchemy flask_migrate


**Database Setup and Seeding**

1. Initialize the database migrations:


    i. flask db init
    ii. flask db migrate -m "Initial migration"
    iii.flask db upgrade

2. Seed the database:

Run the seed.py script to populate the database with initial data from the_show.csv:


python seed.py


**Running the Application**

To start the Flask server, run:

python app.py

The application will be available at http://127.0.0.1:5555.



**API Endpoints**

***GET /episodes***

Retrieve a list of all episodes.

Request: GET /episodes

Response:


[
  {
    "id": 1,
    "date": "1/11/99",
    "number": "1"
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": "2"
  }
]
***GET /episodes/***
Retrieve details for a specific episode, including guest appearances.

Request: GET /episodes/1

Response:


{
  "id": 1,
  "date": "1/11/99",
  "number": "1",
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "episode_id": 1,
      "guest_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}

***GET /guests***

Retrieve a list of all guests.

Request: GET /guests

Response:


[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "comedian"
  }
]


***POST /appearances***

Create a new appearance, linking a guest to an episode with a rating.

Request: POST /appearances


{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}
Response:


{
  "id": 162,
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2,
  "episode": {
    "id": 1,
    "date": "1/11/99",
    "number": "1"
  },
  "guest": {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "comedian"
  }
}

**Validation Error Response:**


{
  "errors": ["validation errors"]
}


**Models**

Episode
1. id: Primary Key, Integer
2. date: String, Non-null
3. number: String, Non-null
4. appearances: Relationship with Appearance (many-to-many)

**Guest**
1. id: Primary Key, Integer
2. name: String, Non-null
3. occupation: String, Non-null
4. appearances: Relationship with Appearance (many-to-many)

**Appearance**
1. id: Primary Key, Integer
2. rating: Integer, between 1 and 5
3. episode_id: Foreign Key to Episode
4. guest_id: Foreign Key to Guest


**License**
This project is licensed under the MIT License. See the LICENSE file for details.

