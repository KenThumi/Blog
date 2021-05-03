import unittest
from app.models import Comment,User,Post

class CommentModelTest(unittest.TestCase):
    ''' Test if model Comment is working well'''

    def setUp(self):
        '''setup Model instances'''
        self.new_user = User(email='ken@gmail.com', username='Kena', password = 'passward')
        self.post = Post(title='Lorem',description='Lorem Ipsum',image='lorem.jpeg',user_id=self.new_user.id, created_at='05:32 PM     02 May 2021')
        self.comment = Comment(comment='Comment Lorem',post_id=self.post.id)

    def tearDown(self):
        Comment.query.delete()
        Post.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertIsInstance(self.comment, Comment)