from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Malatok Dark Lord of the Flayed'} # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Demon Major Belial'},
            'body': 'Beautiful day in the seventh circle of Lord Abaddon\'s Domain!'
        },
        {
            'author': {'nickname': 'High Lord Disarticulator Moloch'},
            'body': 'Human sacrifice is cool!'
        }
    ]
    return render_template("index.html",
                           title='Hell',
                           user=user,
                           posts=posts)
