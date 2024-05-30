# Flight API

This project is a simple REST API for managing flight data using FastAPI and MySQL.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flight-api.git
   cd flight-api
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configure your MySQL database settings in `app/config.py`.

4. Run the database migration script:

   ```bash
   python migrations/create_flights_table.py
   ```

5. Start the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /api/v1/flights`: Add a new flight.
- `GET /api/v1/flights/{flight_no}`: Retrieve a flight by its flight number.

## Authentication

Use the header `X-API-KEY: secret` to authenticate requests.

## Running Tests

Run the tests with the following command:

```bash
python -m unittest discover tests
```
