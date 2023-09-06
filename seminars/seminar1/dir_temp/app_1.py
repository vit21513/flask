from main import app


#
# @app.route("/name/")
# def nike():
#     return f"hello name"

@app.route("/")
def index():
    return "Hello people"


@app.route("/2/")
def nike():
    return f"hello Two"


@app.route("/4/")
@app.route("/3/")
@app.route("/1/")
def two():
    return f"hello first"


if __name__ == '__main__':
    app.run(debug=True)
