from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Matt'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Boston! Sint tempor exercitation enim incididunt pariatur veniam esse nulla ex ex proident labore esse. Esse aliqua pariatur ut velit anim enim excepteur culpa ullamco ea cupidatat adipisicing laboris. Lorem excepteur elit exercitation ullamco voluptate. Culpa incididunt tempor in proident exercitation ex eu cupidatat. Qui minim sunt labore consectetur.'
        },
        {
            'author': {'username': 'Matt'},
            'body': 'Get Out was a really good movie! Irure dolor ipsum occaecat non nulla exercitation. Fugiat mollit esse non nulla cillum irure enim sit occaecat. Laboris commodo minim qui cillum sunt est adipisicing. Veniam duis ipsum cillum nostrud veniam do ad ipsum ex amet ipsum nulla.'
        },
        {
            'author': {'username': 'Matt'},
            'body': 'Get Out was a really good movie! Irure dolor ipsum occaecat non nulla exercitation. Fugiat mollit esse non nulla cillum irure enim sit occaecat. Laboris commodo minim qui cillum sunt est adipisicing. Veniam duis ipsum cillum nostrud veniam do ad ipsum ex amet ipsum nulla.'
        }
    ]
    return render_template('index.html', title='Microblog', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
    