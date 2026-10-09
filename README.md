# Django REST Framework - Train Management API

## Project Overview

This project is a RESTful API developed using Python, Django, and Django REST Framework to manage train information. It supports CRUD (Create, Read, Update, Delete) operations through HTTP methods and returns data in JSON format.

## Features

- **GET:** Retrieve all train records.
- **POST:** Add a new train record.
- **PUT:** Update an existing train record.
- **DELETE:** Delete a train record.
- **Model Serialization:** Convert Django model instances into JSON-compatible data using Django REST Framework serializers.
- **JSON Parsing:** Parse incoming JSON request data using `JSONParser`.
- **Database Integration:** Store and manage train information using a Django model.
- **URL Routing:** Access API endpoints using Django URL patterns.

## Technologies Used

- Python
- Django
- Django REST Framework
- ModelSerializer
- JSON
- SQL Database

## Train Model Fields

The `AllTrain` model contains the following fields:

| Field | Description |
|---|---|
| `trainno` | Train number |
| `trainname` | Train name |
| `start` | Starting station |
| `dest` | Destination station |
| `start_time` | Departure time |
| `end_time` | Arrival time |
| `total_seats` | Total seats |
| `price` | Ticket price |
| `food_supply` | Indicates food availability |

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Retrieve all trains |
| POST | `/` | Add a train |
| PUT | `/<id>/` | Update a train |
| DELETE | `/<id>/` | Delete a train |

Replace `<id>` with the ID of the train record you want to update or delete.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/azadhussain92/Django-REST-Framework-Train-Management-API.git
cd Django-REST-Framework-Train-Management-API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework
```

### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## Testing

You can test the API using:

- Django REST Framework's browsable API (if configured)
- Postman
- cURL

Use JSON request bodies when creating or updating train records.

## Learning Objectives

- Building REST APIs with Django REST Framework
- Implementing CRUD operations
- Using ModelSerializer for serialization
- Handling JSON request data
- Working with Django models and URL routing
- Testing API endpoints using HTTP methods

## Future Improvements

- Add input validation and meaningful error responses.
- Implement Django REST Framework class-based views or viewsets.
- Add authentication and permissions.
- Add pagination and filtering.
- Use appropriate numeric fields for ticket prices and seat counts.

## Disclaimer

This project is intended for learning and practice purposes. It is not connected to a live railway booking system.
