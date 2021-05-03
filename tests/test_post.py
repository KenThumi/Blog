import unittest
from app.models import Post,User

class PostModelTest(unittest.TestCase):
    ''' Test if model Post is working well'''

    def setUp(self):
        '''setup Model instances'''
        self.new_user = User(email='ken@gmail.com', username='Kena', password = 'passward')
        self.post = Post(title='Lorem',description='Lorem Ipsum',image='lorem.jpeg',user_id=self.new_user.id, created_at='05:32 PM     02 May 2021')

    def tearDown(self):
        Post.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertIsInstance(self.post, Post)