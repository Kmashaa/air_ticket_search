from django.test import TestCase
from .models import Flights
import datetime


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.flight = Flights.objects.create(
            id=0,
            aviacompany="MyCompany",
            departure_city="MyCity",
            arrival_city="OtherCity",
            departure_date=datetime.datetime(2001, 1, 1, 1, 1, 1),
            arrival_date=datetime.datetime(2002, 2, 2, 2, 2, 2),
            price=500,
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.flight.aviacompany, str)
        self.assertIsInstance(self.flight.departure_city, str)
        self.assertIsInstance(self.flight.arrival_city, str)
        self.assertIsInstance(self.flight.departure_date, datetime.datetime)
        self.assertIsInstance(self.flight.arrival_date, datetime.datetime)
        self.assertIsInstance(self.flight.price, int)


"""class SignInViewTest(TestCase):
    def test_correct(self):
        response = self.client.post('/signin/', {'username': 'test', 'password': '12test12'})
        self.assertTrue(response.data['authenticated'])
    def test_wrong_username(self):
        response = self.client.post('/signin/', {'username': 'wrong', 'password': '12test12'})
        self.assertFalse(response.data['authenticated'])
    def test_wrong_pssword(self):
        response = self.client.post('/signin/', {'username': 'test', 'password': 'wrong'})
        self.assertFalse(response.data['authenticated'])"""
