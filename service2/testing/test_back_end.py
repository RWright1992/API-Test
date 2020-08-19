import requests
import unittest

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestViews(TestBase):
	def test_view_animal_page(self):
		response = self.client.get(url_for('animal_name'))
		self.assertEqual(response.status_code, 200)

	def test_noisepage_dog(self):
		response = self.client.post(url_for('animal_noise'), data="Dog")
		self.assertIn(b'Woof', response.data)
