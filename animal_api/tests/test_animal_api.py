from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_animal(self):
        for _ in range(20):
            response = self.client.get((url_for('get_animal'))
            self.assertIn(response.data.decode("utf-8"),["cow", "pig", "horse"])

    def test_get_noise(self):
        test_cases =  [("cow", "moo"), ("pig", "oink"), ("horse", "neigh")]
        for case in test_cases:   
            response = self.client.get((url_for('get_animal'), data=[0])
            self.assertIn(response.data.decode("utf-8"),case[1])
    