from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    '''Class to handle user'''

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    posts = db.relationship('Post',backref = 'user',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username} {self.email}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Post(db.Model):
    '''
        Manages a post 
        Args: db.Models
    '''

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.Text)
    comments = db.relationship('Comment',backref = 'post',lazy="dynamic")

    def postowner(self,id):
        if self.user_id == id:
            return True
        else:
            return False

    def __repr__(self):
        return f'Post Title: {self.title}'


class Subscription(db.Model):
    '''
        Manages email subscription
        Args: db.Models
    '''

    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique = True, index=True)

    def __repr__(self):
        return f'Email subscription: {self.email}'



class Comment(db.Model):
    '''
        Manages a comment
        Args: db.Models
    '''

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    

    def __repr__(self):
        return f'Comment: {self.comment}'


