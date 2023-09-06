
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi"


@app.route('/get')
def get():
    if level := request.args.get('level'):

        text = f'your level is big {level}'
    else:
        text = "hi yong gamer"
    return f'{text} {request.args}'


@app.route('/submit', methods= ["GET","POST"])
def submit():
    if request.method == "POST":
        name = request.form.get('name')
        if name =="admin":
            return f'Hello {name}'
        return 'acsess denied'
    return render_template('form.html')

@app.post('/sub')
def submit1():
    name = request.form.get('name')
    return f'Hello {name}'

@app.get('/sub')
def submit_post():
    return render_template('form.html')




if __name__ == "__main__":
    app.run(debug=True)


