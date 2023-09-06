from pathlib import PurePath, Path

from flask import Flask, render_template, request, redirect, abort, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)




@app.route('/')
def index():
    return "Hi"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'files {file_name} upload in server'
    return render_template('upload.html')


@app.errorhandler(404)
def page():
    # app.loger.warning(e)
    contex = {
        'title': 'not found',
        'url': request.base_url},
    return render_template('404.html', **contex), 404



@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Hello {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('task8.html')


if __name__ == '__main__':
    app.run()
