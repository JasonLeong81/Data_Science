from Intro import app
from Intro.models import User, Post
from flask import render_template, url_for, flash, redirect
from Intro.forms import RegistrationForm, LoginForm


p = [
    {'author':'Jason Leong',
     'title':'Blog Post 1',
     'content':'First post content',
     'date_posted':'April 20, 2020'
    },
    {'author':'Yean Chee',
     'title':'Blog Post 2',
     'content':'Second post content',
     'date_posted':'April 21, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=p)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # nothing is wrong or no errors
        flash(f'Account created for {form.username.data}!',category='success')
        return redirect(url_for('home')) # function not route, remember!
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You've been logged in!",'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password.','danger')
    return render_template('login.html',title='Login',form=form)


# set FLASK_APP=run.py # no spaces remember
# set FLASK_DEBUG=1 # changes reload automatically
# flask run