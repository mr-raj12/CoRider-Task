# Flask API with MongoDB

This is a simple Flask application that interacts with MongoDB to manage users. The application allows you to **create**, **read**, **update**, and **delete** users via a RESTful API.

## Features

- **Create User**: Adds a new user to the database.
- **Read Users**: Retrieves all users or a specific user by their ID.
- **Update User**: Updates an existing user's information.
- **Delete User**: Deletes a user from the database.

## Prerequisites

- Python 3.x
- MongoDB (preferrably MongoDB Atlas)
- Flask
- Flask-PyMongo

### Required Packages:

Make sure to install the correct version of `Werkzeug` to avoid compatibility issues:

```bash
pip install werkzeug==2.0.3
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Set up a virtual environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows** (Git Bash/Command Prompt):

  ```bash
  source venv/Scripts/activate
  ```

- **Mac/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

Make sure you're inside the project directory and the virtual environment is activated, then run:

```bash
pip install -r requirements.txt
```

**Important**: As mentioned earlier, if you face issues with `Werkzeug`, run:

```bash
pip install werkzeug==2.0.3
```

### 4. Update MongoDB URI

In the `app.py` file, replace the MongoDB URI with your own MongoDB connection string from MongoDB Atlas (or local MongoDB).

```python
app.config["MONGO_URI"] = "mongodb+srv://your_mongo_uri_here"
```

### 5. Run the Flask app

```bash
python app.py
```

The Flask development server should now be running at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. **Create a User** (POST)

Create a new user by sending a `POST` request to `/users`.

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

**Curl Command**:
```bash
curl -X POST http://localhost:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name":"John Doe", "email":"john.doe@example.com"}'
```

**Response**:
```json
{
  "id": "user_id_here",
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 2. **Get All Users** (GET)

Retrieve a list of all users.

**Curl Command**:
```bash
curl -X GET http://localhost:5000/users
```

**Response**:
```json
[
  {
    "id": "user_id_here",
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
]
```

### 3. **Get a User by ID** (GET)

Retrieve a specific user by their ID.

**Curl Command**:
```bash
curl -X GET http://localhost:5000/users/67b424a7a7357e748c1cf7dc
```

**Response**:
```json
{
  "id": "67b424a7a7357e748c1cf7dc",
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 4. **Update a User** (PUT)

Update an existing user's information. Provide the user ID in the URL and the fields to update in the body.

**Request Body**:
```json
{
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```

**Curl Command**:
```bash
curl -X PUT http://localhost:5000/users/67b424a7a7357e748c1cf7dc \
     -H "Content-Type: application/json" \
     -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
```

**Response**:
```json
{
  "msg": "User updated successfully"
}
```

### 5. **Delete a User** (DELETE)

Delete a user by their ID.

**Curl Command**:
```bash
curl -X DELETE http://localhost:5000/users/67b424a7a7357e748c1cf7dc
```

**Response**:
```json
{
  "msg": "User deleted successfully"
}
```

## Troubleshooting

- **SSL errors with `curl`**: Ensure you're using `http://localhost:5000` instead of `https://localhost:5000` since Flask's default setup doesn't use SSL.
- **MongoDB connection issues**: Make sure your MongoDB URI is correct and your MongoDB server (local or Atlas) is accessible.
- **Werkzeug version issues**: If you encounter compatibility issues, make sure to install `Werkzeug==2.0.3`:

```bash
pip install werkzeug==2.0.3
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.