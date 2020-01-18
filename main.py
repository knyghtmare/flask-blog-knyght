from flask import Flask, render_template
app = Flask(__name__)

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
}
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
