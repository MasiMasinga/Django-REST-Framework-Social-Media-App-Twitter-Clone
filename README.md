# Django REST Framework Social Media Clone (Twitter Clone)

## Description

This is a backend application developed using Django and PostgreSQL. It serves as the API for a social media application that is a clone of Twitter. The application supports user authentication, and allows users to create, read, update, and delete (CRUD) tweets. Users can also comment on tweets and like them.

## Installation

Ensure you have Docker and Docker Compose installed on your machine.

1. Clone the repository:
    ```
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. Build and run the Docker containers:
    ```
    docker-compose up --build
    ```

The application should now be running at `http://localhost:8000`.

## API Endpoints

### Authentication Endpoints

- `POST /api/auth/register`: Register a new user.
- `POST /api/auth/login`: Login a user.
- `GET /api/auth/logout`: Logout a user. 

### Tweets Endpoints

- `GET /api/tweets`: Fetch all tweets.
- `POST /api/tweets`: Create a new tweet.
- `GET /api/tweets/<id>`: Fetch a specific tweet.
- `PUT /api/tweets/<id>`: Update a specific tweet.
- `DELETE /api/tweets/<id>`: Delete a specific tweet.

- `POST /api/tweets/<id>/comments`: Add a comment to a specific tweet.
- `GET /api/tweets/<id>/comments`: Get all comments for a specific tweet.

- `POST /api/tweets/<id>/like`: Like a specific tweet.


## Running the Application Without Docker

If you prefer not to use Docker, you can run the application directly on your machine. Here's how:
    ```

2. Create a virtual environment and activate it:
    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the server:
    ```
    python manage.py runserver
    ```

The application should now be running at `http://localhost:8000`.