import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,PasswordField,SubmitField, ValidationError, TextAreaField,SelectField,FileField #,BooleanField
from wtforms.validators import DataRequired,Email ,Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..models import User,Post
from .. import photos

class PostForm(FlaskForm):
    '''Class to generate post form'''

    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Post', validators=[DataRequired()])
    image = FileField('Upload image',validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])   
    submit = SubmitField('Submit')