"""Utility functions for wrangling data."""

__author__ = "730163077"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        print(row)
        rows.append(row)
    
    file_handle.close()
    return rows


# TODO: Define the other functions here.
def column_values(table: list[dict[str,str]], subject_age: str) -> list[str]:
    """Returns subject_age column values."""
    column_values: list[str, str] = []

    for row in table: 
        column_values.append(str(row["subject_age"]))
    return column_values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforming a table."""
    empty_dict: dict[str,str] = []
    for i in table:
        column_values.append(str(row[i]))
        if i in column_values:
            empty_dict.append(str(row[i]))
    
    return empty_dict
