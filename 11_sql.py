# JOINing data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT population.city, population.population,
              regions.region FROM population, regions WHERE
              population.city = regions.city ORDER BY population.city ASC""")

    rows = c.fetchall()

    display_text = '''City: {}
    Population: {}
    Region: {}

    '''
    for r in rows:
        print(display_text.format(*r))
