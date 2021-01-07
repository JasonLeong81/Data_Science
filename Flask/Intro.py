from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jason'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # three slashes mean current directory

db = SQLAlchemy(app)

class User(db.Model): # will have a table name of user (small u)
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False) # string of max 20 len
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True) # backref is for .lazy is for

    def __repr__(self):
        return f'User( {self.username}, {self.email}, {self.image_file})'

class Post(db.Model): # will have a table name of post (small p)
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #

    def __repr__(self):
        return f"Post( {self.title}, {self.date_posted} )"

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


# set FLASK_APP=Intro.py # no spaces remember
# set FLASK_DEBUG=1 # changes reload automatically
# flask run

if __name__ == '__main__': # another way to run rather than using cmd
    app.run(debug=True)








