# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

class News:
    def __init__(self,title,description, date):
        self.title =title
        self.description = description
        self.date = date


@app.route('/')
def news():
    news = [News('очень новые ноыости','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2'),News('очень новые приколы','описание', '2023-2-2')]
    return render_template('news.html', news =news)


if __name__ == '__main__':
    app.run()
