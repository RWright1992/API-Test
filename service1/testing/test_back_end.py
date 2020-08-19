from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestView(TestBase):

	def test_layout(self):
		response = self.client.get(url_for('layout'))
		self.assertEqual(response.status_code, 200)

	def test_animal(self):
		with patch('requests.get') as g:
			with patch('requests.post') as p:
				g.return_value.text = "Dog"
				p.return_value.text = "Woof"
				response = self.client.get(url_for('animal'))
				self.assertIn(b'Dog', response.data)
				self.assertIn(b'Woof', response.data)
				self.assertEqual(response.status_code, 200)
