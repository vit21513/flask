from main import app


@app.route("/about/")
def about():
    return """ Компания рога и копыта 
               основные виды деятельности производство рогов и копыт"""


@app.route("/contact/")
def contacts():
    return """Номер телефон +799 235 445  
              адрес Красноярск ул. Мичурина 10
                """


if __name__ == '__main__':
    app.run()
