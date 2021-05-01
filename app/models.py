from . import db
from flask_login import UserMixin

class User(db.Models):
'''Class to handle user'''

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    # pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    # comments = db.relationship('Comment',backref = 'user',lazy="dynamic")

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
