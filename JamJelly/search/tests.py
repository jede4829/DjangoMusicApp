from django.test import TestCase
from django.urls import reverse
from . import views

# Create your tests here.

from django.http import HttpRequest

class MyTest(TestCase):
	@classmethod
	def setUp(self):
		self.request= HttpRequest()
		self.request.method="GET"

	#login page: username and password
	def test_a(self):
		response=self.client.get("/")
		self.assertEqual(response.status_code, 200)
	def test_b(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)

	def test_c(self):
		response = self.client.get("/finley")
		self.assertEqual(response.status_code, 404)

	def test_d(self):
		response = self.client.get(reverse('newuser'))
		self.assertEqual(response.status_code, 200)
	
	def test_e(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 404)
	def test_f(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 404)
	def test_g(self):
		response = self.client.get(reverse('do_search'))
		self.assertEqual(response.status_code, 404)
	def test_do_login(self):
		request= HttpRequest()
		request.method="POST"
		request.POST["name"]="jenna1"
		request.POST["password"]="Friday23!"
		response=views.do_login(request)
		self.assertEqual(response.status_code, 200)
	







	#registration page: username, password 2x, client_id, client_secret


