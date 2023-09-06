from flask import Flask

from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def inname(name="хер его знает"):
    return f'ты кто {name.capitalize()}'



@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'path to file {file}'

@app.route('/number/<float:num>/')
def set_num(num):
    print(type(num))
    return f'input number {num}'
@app.route('/text/')
def text():
    return '''<p> <h1>Flask — это микрофреймворк для Python, созданный в <br>2010 году разработчиком по</h1>
имени Армин Ронахер. </h2> Пристава «микро» говорит о том, что Flask действительно<h2/>
маленький. У него в комплекте нет ни набора инструментов, ни библиотек,
которыми славятся другие популярные фреймворки. Но он создан с потенциалом </p>
    '''


if __name__ == '__main__':
    app.run(debug=True)
