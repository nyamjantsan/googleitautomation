#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://raw.githubusercontent.com/google/it-cert-automation-practice/master/Course4/Lab4/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
   "Returns the employees that started on the given date, or the closest one."
 
   data = get_file_lines(FILE_URL)
   reader = csv.reader(data[1: ])
   list_date = list(reader)
   list_date.sort(key = lambda x: x[3])
 
   # We want all employees that started at the same date or the closest newer
   # date.To calculate that, we go through all the data and find the
   # employees that started on the smallest date that 's equal or bigger than
   # the given start date.
 
   min_date = datetime.datetime.today()
   min_date_employees = []
   row_date = []
 
   for row in list_date:
        if datetime.datetime.strptime(row[3], '%Y-%m-%d') >= start_date and datetime.datetime.strptime(row[3], '%Y-%m-%d'):
            row_date.append(row[3])
            min_date_employees.append("{} {}".format(row[0], row[1]))
            return row_date, min_date_employees
def list_newer(start_date):
    start_date, employees = get_same_or_newer(start_date)
    for i in range(0, len(start_date)):
     print("Started on {}: {}".format(start_date[i], employees[i]))                

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
