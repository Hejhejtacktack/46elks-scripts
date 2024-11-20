import csv


def csv_to_list(file_path):
    try:
        with open(file_path, mode='r') as file:
            rows = [row[0] for row in csv.reader(file)]
    except FileNotFoundError:
        raise FileNotFoundError("File not found: {0}".format(file_path))
    except OSError as os_e:
        raise OSError("An error occurred while reading the CSV file: {0}".format(os_e))

    return rows