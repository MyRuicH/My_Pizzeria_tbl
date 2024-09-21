from flask import Flask, render_template


app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


@app.get("/")
def index():
    return render_template("index.html", title="AlfreDDo Pizza| Головна")


@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "Пепероні", "ingredients": "ковбаса 'Пепероні', сир, соус", "price": 150},
        {"name": "Моцарела", "ingredients": "сир 'Моцарела', соус, петрушка", "price": 173},
        {"name": "Чотири сири", "ingredients": "сир 'Моцарела', сир 'Чедер', сир 'Сологуні', сир 'Пармезан', соус", "price": 267},
        {"name": "Чотири сири", "ingredients": "сир 'Моцарела', сир 'Чедер', сир 'Сологуні', сир 'Пармезан', соус", "price": 311}
    ]
    context = {
        "title":"Menu",
        "pizzas": pizzas
    }
    return render_template("menu.html", **context)


if __name__ == "__main__":
    app.run(debug=True)


 