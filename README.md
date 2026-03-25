# Todo List REST API 
A simple RESTFul Api to manage todos, built with python, Flask and SQLite

## Tech Stack 
- **Python 3.12**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM
- **Flask-Marshmallow**- Serialiation and validation
- **SQLite** - Database


### Project Structure 
```
todo-api/
├── app/
│   ├── __init__.py        # App factory
│   ├── extensions.py      # Flask extensions
│   ├── models.py          # Database models and schemas
│   └── routes/
│       ├── __init__.py
│       └── todos.py       # Todo route handlers
├── instance/
│   └── todos.db           # SQLite database (auto-generated)
├── config.py              # App configuration
├── run.py                 # Entry point
└── requirements.txt       # Project dependencies
```
## Getting Started 

### Prerequisites

Make sure you have python 3.12+ installed on your machine

# Installation 

1.Clone the repository 
```bash
git clone https://github.com/Enock594/Todo_Api.git 
cd Todo_Api
```
2.Create and activate a virtual environment
```bash
python3 -m venv venv or
python -m venv venv

# linux/Mac
source /venv/bin/activate
# Windows
source/Scripts/activate
```
3.Install dependencies 
```bash 
pip install -r requirements.txt 
```
4.Create a '.env' file in the project root
```bash
SECRET_KEY=your-secret=key-here
DATABASE_URL='sqlite:///todos.db'
```

## API Endpoints

|Method  | Endpoint | Description|
|--------|----------|------------|
|GET|'/todos'|Get all to-dos|
|GET|'/todos/<id>'|Get a single to-do|
|POST|'/todos'|Create to-dos|
|PUT|'/todos/<id>'|Update a to-do|
|DELETE|'/todos/<id>'|Delete to-do|

## Request & Response Examples

### Create a To-Do

**Request**
```bash
POST /todos/
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

**Response** `201 Created`
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2025-03-23T10:00:00",
  "updated_at": "2025-03-23T10:00:00"
}
```

### Get All To-Dos

**Request**
```bash
GET /todos/
```

**Response** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2025-03-23T10:00:00",
    "updated_at": "2025-03-23T10:00:00"
  }
]
```

### Update a To-Do

**Request**
```bash
PUT /todos/1
Content-Type: application/json

{
  "completed": true
}
```

**Response** `200 OK`
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": true,
  "created_at": "2025-03-23T10:00:00",
  "updated_at": "2025-03-23T10:15:00"
}
```

### Delete a To-Do

**Request**
```bash
DELETE /todos/1
```

**Response** `200 OK`
```json
{
  "message": "Todo 1 deleted successfully"
}
```

## Error Responses

| Status Code | Meaning |
|-------------|---------|
| `400` | Bad request — missing or malformed JSON body |
| `404` | Not found — the requested to-do does not exist |
| `422` | Validation error — a required field is missing or invalid |

**Example validation error**
```json
{
  "errors": {
    "title": ["Missing data for required field."]
  }
}
```




 









