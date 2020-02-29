'''
Homework
1. Using the count() function, calculate the total number of orders for each make and model

2. Output the car's make and model on one line, the quantity on another line, and then the order count on the next line. 
'''

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # 1. Grab order count for each model
    cursor.execute("SELECT make, model, COUNT(*) as order_count FROM orders GROUP BY model")

    rows = cursor.fetchall()

    for r in rows:
        print(*r)

    # 2. output car's make model quantity and order count
    cursor.execute("SELECT i.make, i.model, i.quantity, COUNT(*) as order_count FROM orders as o \
                   INNER JOIN inventory as i on o.model = i.model GROUP BY i.model")

    rows = cursor.fetchall()

    order_count_text = '''Car: {} {}
    Quantity: {}
    Order Count: {}
    ___
    '''

    for r in rows:
        print(order_count_text.format(*r))
