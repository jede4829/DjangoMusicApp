
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from search.models import Profile

test_models = True

class ProfileModelTest(TestCase):
	
	if test_models:
		
		@classmethod
		def setUp(self):
			self.user = User.objects.create_user("Chuckie Finster", "","Friday23!") 
			self.user.profile.client_id="1234"
			self.user.profile.client_secret="5678"
			self.user.save()

		def test_it_has_info_fields(self):
			#self.assertIsInstance(self.profile.user,str)
			self.assertEqual(self.user.username, 'Chuckie Finster')
			self.assertEqual(self.user.profile.client_id, '1234')
			self.assertEqual(self.user.profile.client_secret, '5678')

		def test_login(self):
			user = authenticate(username="Chuckie Finster", password="Friday23!")
			self.assertEqual(user.username, "Chuckie Finster")
			self.assertTrue(user)
			self.assertEqual(self.user.profile.client_id, '1234')
			self.assertEqual(self.user.profile.client_secret, '5678')

		def test_failed_login(self):
			user = authenticate(username="Chuckie Finster", password="friday23!")
			self.assertTrue(user==None)

		def test_failed_login2(self):
			user = authenticate(username="chuckie Finster", password="Friday23!")
			self.assertTrue(user==None)

		def test_failed_login3(self):
			user = authenticate(username="", password="")
			self.assertTrue(user==None)

		def test_failed_login4(self):
			user = authenticate(username=None, password=None)
			self.assertTrue(user==None)
