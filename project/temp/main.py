import json
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, redirect, url_for, flash
from flask import request
from flask import render_template

app = Flask(__name__, static_folder='static')
app.secret_key = b'55849b73a017e1a5d7f09ff7f14c1e5d9fc58685776a345530c6ed325d05df96'


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/geo/')
def geo():
    return render_template('galerey.html')


@app.route('/galereia/')
def galereia():
    return render_template('galerey.html')


@app.route('/invent/')
def invent():
    return render_template('galerey.html')


@app.route('/cadastr/')
def cadastr():
    return render_template('galerey.html')


@app.route('/project/')
def project():
    return render_template('galerey.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/order/', methods=['GET', 'POST'])
def order():
    options = ['Земельный участок', 'Жилой дом, Квартира', 'Иное', 'Задать вопрос']
    if request.method == 'POST':
        # Получаем данные из формы
        selected_option = request.form['selectedOption']
        last_name = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        # Создаем словарь с данными, включая выбранный элемент списка
        data = {
            'Выбранный элемент': selected_option,
            'Имя Фамилия': last_name,
            'Email адрес': email,
            'Номер телефона': phone,
            'Сообщение': message
        }
        flash('Ваше обращение отправлено',"success")
        save_to_json(data)
        return redirect(url_for('order'))
    return render_template('orders.html', options=options)


def save_to_json(data):
    # Путь к файлу для сохранения данных
    file_path = 'data.json'
    # Создаем или открываем файл и записываем данные в формате JSON
    with open(file_path, 'a', encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False,indent=1)
        file.write('\n')


if __name__ == '__main__':
    app.run(debug=True)
