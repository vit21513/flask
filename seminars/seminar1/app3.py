# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму


from app1 import app


# @app.route("/summa/<number>")

@app.route('/<int:num1>/<int:num2>')
def summa(number):
    a, b, *_ = number.split()
    return f'Cумма введеных чисел  {int(a) + int(b)}'


@app.route('/<int:num_a>/<int:num_b>')
def hello(num_a, num_b):
    return f'{num_a} + {num_b} = {num_a + num_b}'


@app.route("/<text>/")
def lens_text(text):
    return f'Длина строки {len(text)}'


if __name__ == '__main__':
    app.run()
