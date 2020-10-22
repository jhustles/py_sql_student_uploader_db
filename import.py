# Write a program that imports data from a CSV spreadsheet

import sys
import csv
import re
import sqlite3 as sl

def main():
# Validate correct inputs for command line argument (CLA), otherwise notify of error and exit
    if len(sys.argv) != 2:
        sys.exit("Usage Error: python import.py file.csv")

    # Open the inputted csv file in the CLA
    csvpath = open(sys.argv[1])

    data = csv.DictReader(csvpath)

    student_data = []
    for row in data:
        # Parse name using regex and split method
        name_tuple = row['name'].split(' ')
        name_tuple.append(row['house'])
        name_tuple.append(row['birth'])
        #print(name_tuple)
        student_data.append(name_tuple)
    #print(name_tuple)

    name_tuple_w_none = []
    for i in student_data:
        tmp_array = []
        if len(i) == 4:
            tmp_array.append(i[0])
            tmp_array.append(None)
            # tmp_array.append(i[1])
            # tmp_array.append(i[2])
            # tmp_array.append(i[3])
            tmp_array.extend(i[1:4])
            updated_name_tuple = tuple(tmp_array)
            name_tuple_w_none.append(updated_name_tuple)
        else:
            name_tuple_w_none.append(i)


    # Checking for desired output
    # for i in name_tuple_w_none:
    #     print(len(i))
    # print(len(name_tuple_w_none))
    # print(name_tuple_w_none)

    # SQLite3 - Connect to it
    con = sl.connect('students.db')
    # print(con)

    insert_q = 'INSERT INTO students (first, middle, last, house, birth) values (?, ?, ?, ?, ?)'

    with con:
        #Connect to SQLite3 DB - execute many takes two agruments: Insert Query Command and the Data (aka name_tuple_w_none)
        con.executemany(insert_q, name_tuple_w_none)
        #print("Completed inserting")
        # query_results = con.execute("SELECT * FROM students")
        # for row in query_results:
        #     print(row)
        # con.execute("SELECT * FROM students")


main()