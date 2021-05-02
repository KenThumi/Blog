from . import main
from flask import render_template,redirect,url_for, flash,request,abort
from flask_login import login_required, current_user
from ..models import User,Post, Subscription
from .. import db,photos
from .forms import PostForm
from datetime import datetime
from sqlalchemy import desc
from ..email import mail_message


@main.route('/')
def home():
    '''Home route'''

    recentpost = Post.query.order_by(desc(Post.id)).first()
    # created_at = datetime.fromtimestamp( int(recentpost.created_at )).strftime('%I:%M %p     %d %b %Y')


    posts = Post.query.order_by(desc(Post.id)).all()


    return render_template('index.html', recentpost=recentpost, posts=posts)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/addpost', methods=['GET', 'POST'])
@login_required
def addpost():
    form = PostForm()
    
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.description.data,user_id=current_user.id,created_at=datetime.now().strftime('%I:%M %p     %d %b %Y')  )   #datetime.now().timestamp()
       
        filename = photos.save(form.image.data)
        path = f'photos/{filename}'
        
        post.image = path

        db.session.add(post)

        db.session.commit()

        notify()

        flash('Post submitted successfully','success')


    return render_template('post.html', form=form)



@main.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    # print(request.form.get('email'))
    subscription = Subscription(email=request.form.get('email'))
    
    db.session.add(subscription)
    db.session.commit()

    flash('Subscription submitted successfully','success')

    return redirect(url_for('main.home'))



def notify():
    '''Notifys users of new post'''
    users = Subscription.query.all()

    for user in users:
        mail_message("New Arcticle","email/blog",user.email,user=user)


@main.route('/editpost/<id>', methods=['GET', 'POST'])
@login_required
def editpost(id):
    post = Post.query.get(id)

    form = PostForm()
    
    
    if form.validate_on_submit():
        post = Post.query.get(id)
        post.title = form.title.data
        post.description = form.description.data

        if not not form.image.data:
            filename = photos.save(form.image.data)
            path = f'photos/{filename}'
            post.image = path

        db.session.add(post)

        db.session.commit()

        flash('Post submitted successfully','success')

        return redirect(url_for('main.home'))

    form.title.data = post.title
    form.description.data = post.description

    return render_template('post.html', form=form)




