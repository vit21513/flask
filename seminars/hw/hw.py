from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # Проверяем, есть ли пользователь с таким email в базе данных
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return 'Пользователь с таким email уже существует!'

        # Хешируем пароль
        hashed_password = sha256_crypt.hash(password)

        # Создаем нового пользователя
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)

        # Сохраняем пользователя в базе данных
        db.session.add(new_user)
        db.session.commit()

        return 'Вы успешно зарегистрированы!'

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)