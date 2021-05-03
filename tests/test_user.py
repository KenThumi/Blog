import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(email='ken@gmail.com', username='Kena', password = 'passward')

    def tearDown(self):
        User.query.delete()

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('passward'))



