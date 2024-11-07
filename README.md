# jwt_practice

This is a simple Flask application that demonstrates JWT authentication.

## Prerequisites

- Python 3.x
- Flask
- PyJWT

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/jwt_practice.git
   cd jwt_practice
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Set the Flask app environment variable:

   ```sh
   export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
   ```

2. Run the Flask application:

   ```sh
   flask run
   ```

3. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Endpoints

- `GET /` - Home page, redirects to login if not authenticated.
- `GET /public` - Public page, accessible without authentication.
- `GET /auth` - Protected page, requires a valid JWT token.
- `POST /login` - Login endpoint, returns a JWT token if credentials are valid.

## Usage

1. Navigate to the home page and log in with the following credentials:

   - Username: `admin`
   - Password: `1234`

2. After logging in, you will receive a JWT token. Use this token to access the protected `/auth` endpoint by including it as a query parameter:

   ```sh
   curl -H "Authorization: Bearer <your_token>" http://127.0.0.1:5000/auth
   ```

## License

This project is licensed under the MIT License.
