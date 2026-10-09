"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv
import os


def read_csv_file(filepath):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    # TODO: Your code here
    try:
            with open(filepath, "r") as file:
                 return list(csv.DictReader(file))
    except FileNotFoundError:
            print(f"{filepath} not found. Starting with an empty csv file.")
    except csv.Error:
            print("Error reading CSV file.")

    # Hint: Use csv.DictReader to read CSV files into dictionaries
    # Hint: Remember to use 'with open()' for proper file handling


def count_records(data_list):
    """Counts the number of records in a dataset."""
    # TODO: Your code here
    return len(data_list)

    # Hint: Use the len() function


def get_unique_values(data_list, field_name):

    unique_values = set()
    for record in data_list:
      unique_values.add(record[field_name])
    return sorted(unique_values)
    # Hint: Use a set to collect unique values
    # Hint: Convert the set to a list and sort it before returning


def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""
    # TODO: Your code here
    return [record for record in data_list if record[field_name] == field_value]
    # Hint: Use a list comprehension to filter or a loop!
    # see here for more info: https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions


def calculate_total(data_list, field_name):
    """Calculates the sum of a numeric field across all records."""
    # TODO: Your code here
    total = 0
    # Hint: Initialize a total variable to 0
    # Hint: Loop through each record and add float(record[field_name]) to total
    # Hint: Remember to convert string values to float!
    for record in data_list:
        total += float(record[field_name])
    return total


def calculate_average(data_list, field_name):
    """Calculates the average value of a numeric field."""
    # TODO: Your code here
    # Hint: Use calculate_total() and count_records() functions
    # Hint: Average = total / count
    total = calculate_total(data_list, field_name)
    count = count_records(data_list)
    return total / count if count > 0 else 0                                        


def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    # TODO: Your code here
    # Hint: Loop through data_list
    # Hint: Return the record when record[id_field] == id_value
    for record in data_list:
        if record[id_field] == id_value:
            return record   
    return None 

def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    # TODO: Your code here
    # Hint: Create a dictionary mapping secondary_list IDs to records
    # Hint: For each record in primary_list, look up the matching secondary record
    # Hint: Use dict.update() to merge dictionaries
    primary_dict = {record[primary_key]: record for record in primary_list}
    secondary_dict = {record[foreign_key]: record for record in secondary_list}
    for key, primary_record in primary_dict.items():
        if key in secondary_dict:
            primary_record.update(secondary_dict[key])

def write_report_to_file(filepath, report_content):
    # Extract the directory path and create it if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(report_content)   

def format_header(title):
    """Creates a formatted header for reports."""
    # TODO: Your code here
    # Hint: Use "=" * 60 to create a line of equals signs
    # Hint: Use .center(60) to center the title
    line = "=" * 60
    return f"{line}\n{title.center(60)}\n{line}\n"


# Testing functions
if __name__ == '__main__':
    print("Testing report functions...")
    print("Implement functions above, then uncomment test code below")
    
    # # Test read_csv_file
    # pilots = read_csv_file('../data/pilots.csv')
    # print(f"Loaded {len(pilots)} pilots")
