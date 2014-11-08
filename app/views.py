from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'sweetrain'}    #fake user
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beuatiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The avengers movie was so coooool!'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                            title='Sign In',
                            form=form)
