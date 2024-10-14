# SA.-Phase-4-Code-Challenge-Late-Show. 
Step 1: Create the React app.
    - Run npx create-react-app frontend in my terminal to create a new React app.
    - Navigated to the frontend folder and removed unnecessary files (e.g., logo.svg, App.test.js) for a cleaner work.

Step 2: Install dependencies.
    - react-router-dom for routing: npm install react-router-dom
    - axios for making HTTP requests: npm install axios
    - redux, react-redux for state management: npm install redux react-redux


Step 3: Set up the Backend (Flask).
 A. Create a Flask app. 

     - Created a backend folder and set up a virtual environment:
         = mkdir backend
         = cd backend
         = python3 -m venv venv
         = source venv/bin/activate
    - Install Flask and necessary libraries:
         = pip install Flask Flask-CORS Flask-SQLAlchemy Flask-JWT-Extended

 B. Make Flask file structure
     - In the backend folder, create a structure:
        backend/
          ── app.py
          ── models.py
          ── routes.py
          ── config.py


Step 4: Create basic endpoints for login, register, and CRUD operations

Step 5: JWT Authentication
    - This has already been covered in the above step by using JWTManager, create_access_token, and jwt_required.


Step 6: Frontend Routes and Authentication

