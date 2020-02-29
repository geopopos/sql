'''
Homework
________
1. use the "inventory" table from the previous homework assignment, add 5 records to the table. Make sure 3 of the vehicles are Fords while the other 3 are Hondas. Use any model and quantity of each.
2. Update the quantity on two of the records, and then output all of the records from the table.
3. output only records tha are for Ford vehicles.
'''

import sqlite3

def print_rows(c, query):
    c.execute(query)

    rows = c.fetchall()

    for r in rows:
        print(*r)

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create inventory list
    cars = [
        ('Ford', 'Focus ST', 7),
        ('Ford', 'Edge ST', 2),
        ('Ford', 'F-150', 1),
        ('Honda', 'Civic Type-R', 1),
        ('Honda', 'Accord', 22)
    ]

    # Add inventory to database from list
    c.executemany('INSERT INTO inventory (make, model, quantity) VALUES(?, ?, ?)', cars)

    print("1. Inventory")
    print_rows(c,"SELECT make, model, quantity FROM inventory")

    # update the quantity on two of the records, and then output all of the records from the table.
    c.execute("UPDATE inventory SET quantity=6 WHERE model = 'Focus ST'")
    c.execute("UPDATE inventory SET quantity=21 WHERE model = 'Accord'")

    print("2. Updated Inventory")
    print_rows(c,"SELECT make, model, quantity FROM inventory")

    # output only the records that are Fords
    
    print("3. Make Ford Inventory")
    print_rows(c, "SELECT make, model, quantity FROM inventory WHERE make='Ford'")


