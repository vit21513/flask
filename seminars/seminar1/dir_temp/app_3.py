from flask import Flask

from flask import render_template

app = Flask(__name__, static_folder='templates')


@app.route('/')
@app.route('/index/')
def html():
    return render_template('index1.html')





# @app.route('/index/')
# def html_index():
#     context = {
#         'title':'личный блог',
#         'name':'харитон',
#         'value':[1,2,3,4,56,7,8,9]
#     }
#     return render_template('index.html', **context)

@app.route('/two/')
def html_two():
    context = {
        'title': 'личный блог',
        'name': 'харитон',
        'value': [1, 2, 3, 4, 56, 7, 8, 9]
    }

    return render_template('two.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
