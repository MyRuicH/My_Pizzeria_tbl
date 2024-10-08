from flask import Flask, render_template, request

from app.data import db

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


@app.get("/")
def index():
    return render_template("index.html", title="AlfreDDo Pizza| Головна")


@app.get("/menu/")
def menu():
    pizzas = db.get_pizzas()
    context = {
        "title":"Меню",
        "pizzas": pizzas
    }
    return render_template("menu.html", **context)


@app.get("/add_pizza/")
def add_pizza():
    return render_template("add_pizza.html", title="Додати піцу")


@app.post("/add_pizza/")
def add_pizza_post():
    data = request.form
    print(f"{data = }")
    db.insert_data(**data)
    index()


if __name__ == "__main__":
    app.run(debug=True)


 