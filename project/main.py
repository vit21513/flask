
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
import json
import os
import random
import string
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from content_site import cadastre_dom, cadaste_zem, cadaste_act, invent_text, geo_site, project_site, gal_content
from flask_mail import Mail, Message
from threading import Thread
import logging

# Настройки логирования

logging.basicConfig(filename='email_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 465  # Порт SMTP-сервера
app.config['MAIL_USE_SSL'] = True  # Использовать TLS
app.config['MAIL_USERNAME'] = 'testroscadastr@mail.ru'
app.config['MAIL_PASSWORD'] = 'VTCvuAWkcnDipihw0hFT'
mail = Mail(app)

# 'Qqeryuo98765'
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/geo/')
def geo():
    return render_template('geodesia.html', geo_site=geo_site)


@app.route('/galereia/')
def galereia():
    return render_template('galerey.html', gal_content=gal_content)


@app.route('/invent/')
def invent():
    return render_template('invent.html', invent_text=invent_text)


@app.route('/cadastr/')
def cadastr():
    return render_template('cadastr.html', cadaste_zem=cadaste_zem, cadastre_dom=cadastre_dom, cadaste_act=cadaste_act)


@app.route('/project/')
def project():
    return render_template('project.html', project_site=project_site)


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


def generate_captcha():
    width, height = 200, 100
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    font = ImageFont.truetype('arial.ttf', 36)
    text_width = 100
    text_height = 50
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Рисуем текст на изображении
    draw.text((x, y), captcha_text, font=font, fill=(0, 0, 0))
    # Добавляем небольшой шум к изображению
    for _ in range(100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(0, 0, 0))
    image.save('static\captcha.png')
    return captcha_text


class OrderForm(FlaskForm):
    selected_option = SelectField('Выберите опцию', choices=[
        ('Земельный участок', 'Земельный участок'),
        ('Жилой дом', 'Жилой дом'),
        ('Квартира', 'Квартира'),
        ('Иное', 'Иное'),
        ('Задать вопрос', 'Задать вопрос')
    ], validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Телефон', validators=[DataRequired()])
    message = StringField('Сообщение', validators=[DataRequired()])
    captcha = StringField('Проверочный код', validators=[DataRequired()])
    submit = SubmitField('Отправить')


def send_email_in_thread(text):
    try:
        msg = Message('Форма заказа', sender='testroscadastr@mail.ru', recipients=['vit21513@yandex.ru'])
        msg.body = text
        with app.app_context():
            mail.send(msg)
    except Exception as e:
        # Записываем событие и время в лог файл
        logging.error(f'Ошибка отправки электронной почты: {str(e)}')


@app.route('/order/', methods=['GET', 'POST'])
def order():
    options = ['Земельный участок', 'Жилой дом, Квартира', 'Иное', 'Задать вопрос']
    form = OrderForm()
    if form.validate_on_submit():
        captcha = form.captcha.data
        if captcha == request.cookies.get('captcha'):
            # Получаем данные из формы
            selected_option = form.selected_option.data
            last_name = form.last_name.data
            email = form.email.data
            phone = form.phone.data
            message = form.message.data
            # Создаем словарь с данными, включая выбранный элемент списка
            data = {
                'Выбранный элемент': selected_option,
                'Имя Фамилия': last_name,
                'Email адрес': email,
                'Номер телефона': phone,
                'Сообщение': message,
                'Дата создания': str(datetime.now())
            }
            flash('Ваше обращение отправлено', "success")
            save_to_json(data)
            # Отправка письма в отдельном потоке
            thread = Thread(target=send_email_in_thread, args=(str(data)[1:-1],))
            thread.start()
            response = make_response(redirect(url_for('order')))
            response.set_cookie('captcha', '', expires=0)  # Удаляем куку с капчей
            return response
        else:
            flash('Неправильный проверочный код', "warning")
    # Генерируем капчу и сохраняем в куки
    captcha = generate_captcha()
    response = make_response(render_template('orders.html', form=form, options=options, captcha=captcha))
    response.set_cookie('captcha', captcha)
    return response


def save_to_json(data):
    # Загружаем текущие заказы (если есть)
    try:
        with open('orders.json', 'r', encoding="UTF-8") as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = []
    # Добавляем новый заказ
    orders.append(data)
    # Сохраняем заказы обратно в файл
    with open('orders.json', 'w', encoding="UTF-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=1)




if __name__ == '__main__':
    app.run()
