from flask import render_template, url_for, flash, redirect
from knyghtblog import app
from knyghtblog.forms import RegistrationForm, LoginForm
from knyghtblog.models import User, Post

# dummy data
posts = [
{
    'post_title'  : "Richard Madden",
    'post_author' : 'Faria Tahsin',
    'post_content': 'I love Richard Madden.',
    'post_date'   : 'December 25th, 2019'
},
{
    'post_title'  : "Guild Wars 2",
    'post_author' : 'Knyght',
    'post_content': 'Guild Wars 2 was an epic game, but it sort of sucks now.',
    'post_date'   : 'January 3, 2020'
},
{
    'post_title'  : "Naisa",
    'post_author' : 'Omer Fahim',
    'post_content': 'She is the love of my life.',
    'post_date'   : 'January 19, 2020'
},
{
    'post_title'  : "Jason Momoa",
    'post_author' : 'Mahnaz Rashid',
    'post_content': "Jason Momoa is the world's most perfect man.",
    'post_date'   : 'January 10, 2020'
},
{
    'post_title'  : "Cyberpunk 2077",
    'post_author' : 'Ishtyman',
    'post_content': "Gotta play Cyberpunk 2077 when it comes out.",
    'post_date'   : 'January 19, 2020'
}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect( url_for('home') )
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
