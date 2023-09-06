# ... (ваш импорт и настройки)

# ... (ваш остальной код)

# Функция для отправки письма в отдельном потоке
def send_email_in_thread(text):
    msg = Message('Форма заказа', sender='testroscadastr@mail.ru', recipients=['vit21513@yandex.ru'])
    msg.body = text
    with app.app_context():
        mail.send(msg)

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

# ... (ваш остальной код)

if __name__ == '__main__':
    app.run(debug=True)
