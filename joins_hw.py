'''
JOIN homework
1.
  a. Add another table to your cars database called orders
     should have the follwing fields
       make        TEXT
       model       TEXT
       order_date  DATE (Sqlite3 does not have datatypes for dates, we can use SQLite functions for comparing date values
  b. add 15 records (3 for each car), each with separate order dates

2. Output the car's make and model on one line, the quantity on another line, and then the
   order_dates on the subsequent lines.
   ex:
       Car: Ford Focus ST
       Quantity: 7
       Orderdates:
           2020-01-23
           2020-02-23
'''

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders (make TEXT, model TEXT, order_date  TEXT)""")

    orders = [
        ('Ford', 'Focus ST', '2020-01-23'),
        ('Ford', 'Focus ST', '2020-01-07'),
        ('Ford', 'Focus ST', '2020-02-29'),
        ('Ford', 'Edge ST', '2020-02-27'),
        ('Ford', 'Edge ST', '2020-01-01'),
        ('Ford', 'Edge ST', '2020-02-04'),
        ('Ford', 'F-150', '2020-02-05'),
        ('Ford', 'F-150', '2020-01-26'),
        ('Ford', 'F-150', '2020-02-23'),
        ('Honda', 'Civic Type-R', '2020-02-14'),
        ('Honda', 'Civic Type-R', '2020-01-21'),
        ('Honda', 'Civic Type-R', '2020-02-21'),
        ('Honda', 'Accord', '2020-02-09'),
        ('Honda', 'Accord', '2020-01-22'),
        ('Honda', 'Accord', '2020-02-01')
    ]

    c.executemany("INSERT INTO orders (make, model, order_date) VALUES(?, ?, ?)", orders)

    order_text = '''Car: {} {}
Quantity: {}
Order Dates:
        {}
___
     '''

    c.execute("""SELECT i.make, i.model, i.quantity, GROUP_CONCAT(o.order_date, '\n\t') order_dates
              FROM orders as o INNER JOIN inventory as i on i.make = o.make AND i.model = o.model
              GROUP BY i.make, i.model""")

    rows = c.fetchall()

    for r in rows:
        print(order_text.format(*r))

