import os

import csv

reader = csv.reader(open('Resources/students_complete.csv'), delimiter=",")

import pandas as pd

df = pd.read_csv('Resources/students_complete.csv')

print(df.head())

df = pd.read_csv('Resources/students_complete.csv')

df = df.sort_values(by=['math_score'], ascending=False)

for math_score in reader:
    print(df.head())

df = pd.read_csv('Resources/students_complete.csv')

df = df.sort_values(by=['reading_score'], ascending=True)

for reading_score in reader:
    print(df.head())

def linear_search_csv(filename, search_term, column_name):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        matching_rows = []

        for row in reader:
            if row[column_name] == search_term:
                matching_rows.append(row)

    return matching_rows

if __name__ == "__main__":
    search_term = input("Enter the Student ID: ")
    column_name = input("Enter the column to search: ")

    result = linear_search_csv(filename, search_term, column_name)

    if result:
        print("Matching rows:")
        for row in result:
            print(row)
    else:
        print("No matching rows found.")