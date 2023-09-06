# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

from pathlib import PurePath, Path

from flask import Flask, render_template, request, abort, url_for, flash
from werkzeug.utils import secure_filename, escape, redirect

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/hello/')
def hello1():
    return 'hello'




@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'static/img', file_name))
        return render_template('task2_1.html', file_name=file_name)
    return render_template('task2.html')


users ={'admin':"1234"}

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username, password) in users.items():
            return 'Вы вошли'
        return f'Неправильный {escape(username)} логин или пароль'
    return render_template('task3.html')

@app.route('/count/', methods=['GET', 'POST'])
def count():
    if request.method == 'POST':
        text = request.form.get('text')
        count = len(text.split())
        return f"Количество слов: {count}"
    return render_template('task4.html')

@app.route('/culc/', methods=['GET', 'POST'])
def culc():
    if request.method == 'POST':
        number1 = int(request.form.get('number1'))
        number2 = int(request.form.get('number2'))
        operation = request.form.get('operation')
        if operation == 'add':
            return f"{number1 + number2}"
        elif operation == 'subtract':
            return f"{number1 - number2}"
        elif operation == 'multiply':
            return f"{number1 * number2}"
        elif operation == 'divide':
            return f"{number1 / number2}"
    return render_template('task5.html')


@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        username = request.form.get('username')
        age = int(request.form.get('age'))
        if age < 18:
            return abort(403)
        return f"{username}, {age} возраст прошел"
    return render_template('task6.html')

@app.errorhandler(403)
def age_age_not(e):
    print(e)
    return render_template('403.html'), 403

@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        result = number**2
        return redirect(url_for('square_result', result=result))
    return render_template('task7.html')

@app.route('/square_result/')
def square_result():
    return request.args.get('result')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Hello {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('task8.html')

if __name__ == '__main__':
    app.run()
