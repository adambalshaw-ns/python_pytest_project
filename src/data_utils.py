import csv
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns a list of dictionaries.
    Each row is a dictionary with column names as keys.
    """
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def get_average_age(data: List[Dict[str, str]]) -> float:
    """
    Calculates the average age from CSV data.
    """
    ages = [int(row['age']) for row in data]
    return sum(ages) / len(ages)

