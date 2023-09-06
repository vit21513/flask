
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def news():
    return render_template('news.html', news =news)

@app.route('/about/')
def about():
    return  render_template("about.html")

if __name__ == '__main__':
    app.run()
