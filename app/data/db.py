import sqlite3


def insert_data(
                name: str|None,
                ingredients: str|None,
                price: int|None=None) -> None:
    
    try:
        sql_con = sqlite3.connect("pizzas.db")
        cursor = sql_con.cursor()

        quary = "INSERT INTO Pizzas(name, ingredients, price) VALUES(?, ?, ?)"
        data = (name, ingredients, price)

        cursor.execute(quary, data)
        sql_con.commit()
        cursor.close()
        print("Дані дадані")
        
    except sqlite3.Error as error:
        print("Виникла помилка:", error)

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою данних упішно завершена!")


def get_pizzas() -> list:
    data = []

    try:
        sql_con = sqlite3.connect("pizzas.db")
        cursor = sql_con.cursor()

        quary = "SELECT * FROM Pizzas;"
        
        cursor.execute(quary)
        data = cursor.fetchall()
        cursor.close()
        print("Дані дадані")
        

    except sqlite3.Error as error:
        print("Виникла помилка:", error)

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою данних упішно завершена!")

        return data




