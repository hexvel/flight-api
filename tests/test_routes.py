import unittest

from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from app import app
from app.database import Base, engine
from app.models import Flight


class FlightRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=engine)

    def test_add_flight(self):
        response = self.client.post(
            "/api/v1/flights",
            headers={"X-API-KEY": "secret"},
            json={
                "flight_no": "FL123",
                "airline": "AirTest",
                "departure_city": "CityA",
                "arrival_city": "CityB",
                "departure_time": "2024-06-01T12:00:00",
                "arrival_time": "2024-06-01T15:00:00",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Flight added successfully"})

    def test_get_flight(self):
        with self.session() as session:
            flight = Flight(
                flight_no="FL123",
                airline="AirTest",
                departure_city="CityA",
                arrival_city="CityB",
                departure_time="2024-06-01T12:00:00",
                arrival_time="2024-06-01T15:00:00",
            )
            session.add(flight)
            session.commit()

        response = self.client.get(
            "/api/v1/flights/FL123", headers={"X-API-KEY": "secret"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "flight_no": "FL123",
                "airline": "AirTest",
                "departure_city": "CityA",
                "arrival_city": "CityB",
                "departure_time": "2024-06-01T12:00:00",
                "arrival_time": "2024-06-01T15:00:00",
            },
        )


if __name__ == "__main__":
    unittest.main()
