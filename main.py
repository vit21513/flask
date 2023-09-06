from flask import Flask

app = Flask(__name__)


@app.route('/')
def hell():
    return 'Привет мир'


if __name__ == '__main__':
    app.run()
