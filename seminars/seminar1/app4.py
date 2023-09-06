# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.


from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# @app.route('/index/')
# def html():
#     hello = "Привет, мир!"
#     text = "Моя первая HTML страница"
#     return render_template('index.html', text_list=text, hello_i=hello)


students = [
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5},
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5},
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5},
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5}
]
@app.route('/')
@app.route('/student/')
def get_studets():
    return render_template("student.html", students= students)

if __name__ == '__main__':
    app.run()
