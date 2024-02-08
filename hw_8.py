import sqlite3


conn = sqlite3.connect('car.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        car_title TEXT NOT NULL,
        price FLOAT DEFAULT 0.0,
        quantity INTEGER DEFAULT 0
    );''')

def add_car(car_title, price, quantity):
    cursor.execute('''
        INSERT INTO cars_list (car_title, price, quantity) VALUES (?, ?, ?)
    ''', (car_title, price, quantity))
    conn.commit()

def delete_car(car_id):
    cursor.execute('''
        DELETE FROM cars_list WHERE id=?
    ''', (car_id,))
    conn.commit()

def get_cheaper_cars():
    cursor.execute('''
        SELECT * FROM cars_list WHERE price < 100
    ''')
    cars = cursor.fetchall()
    for car in cars:
        print(f"Car ID: {car[0]}, Title: {car[1]}, Price: {car[2]}, Quantity: {car[3]}")

add_car('mers', 10, 5)
add_car('bmw', 100, 1)
add_car('bugati', 50, 7)

print ("Cars before deletion:")
get_cheaper_cars()

delete_car(6)  

print("\nCars after deletion:")
get_cheaper_cars()

conn.close()