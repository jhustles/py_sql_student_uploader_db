# Write a program that prints a list of students for a given house in alphabetical order.

import sys
import sqlite3 as sl

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python roster.py <house_name>")
    # print(sys.argv[1])

    con = sl.connect('students.db')
    con.row_factory = dict_factory

    c = con.cursor()
    #insert_query = 'SELECT CASE WHEN middle = "None" THEN (first ||' '|| last) ELSE (first || middle || last) END AS "name", house FROM students WHERE house=?'
    house = (sys.argv[1],)
    # results = c.execute('SELECT CASE WHEN middle = "None" THEN (first ||' '|| last) ELSE (first || middle || last) END AS "name", house FROM students WHERE house=?', house)
    c.execute('SELECT first, middle, last, house, birth FROM students WHERE house=? ORDER BY last', house)
    #print(c.fetchall())

    results = c.fetchall()

    for row in results:
        if row['middle'] != None:
            print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}")
        else:
            print(f"{row['first']} {row['last']}, born {row['birth']}")
    return

    # Functions
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

main()