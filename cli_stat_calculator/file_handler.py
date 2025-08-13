# This module is responsible for:
# Reading CSV files from user input
# Extracting numeric data (for stats)
# Parsing column names and row values (for correlation and hypothesis tests)
# Handling errors such as file not found, invalid values, or wrong format

import csv
import os

class CSVReader:
    @staticmethod
    def load_csv(filepath):
        """
        Loads a single column of numeric data from a CSV file.
        Returns a flat list of values (for statistics like mean, median).
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File '{filepath}' does not exist.")

        data = []
        with open(filepath, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    try:
                        data.append(float(item))
                    except ValueError:
                        continue  # Skip non-numeric values
        if not data:
            raise ValueError("No numeric data found in the CSV.")
        return data

    @staticmethod
    def load_csv_as_dict(filepath):
        """
        Loads the entire CSV file as a dictionary.
        Each key is a column header; value is a list of values.
        Useful for correlation and hypothesis testing.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File '{filepath}' does not exist.")

        with open(filepath, 'r', newline='') as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames:
                raise ValueError("CSV file must contain a header row.")

            data = {header: [] for header in reader.fieldnames}
            for row in reader:
                for key in row:
                    data[key].append(row[key])
        return data


# What This File Covers
# Function	Use
# load_csv()	Loads CSV as a flat list of floats (for univariate stats)
# load_csv_as_dict()	Loads CSV into a dictionary ({column_name: list}) for multi-column analysis
# Error Handling	Missing file, empty file, non-numeric values, no headers

# Error Handling Built In
# Raises FileNotFoundError if the file path is wrong

# Raises ValueError if data is empty or lacks headers

# Skips invalid values quietly in numeric extractions

