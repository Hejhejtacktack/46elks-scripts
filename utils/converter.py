import csv


def csv_to_list(file_path):
    """
    Takes a file path to a csv file and returns a list of lists.
    :param file_path: the file path of the csv file
    :return: a list of strings hopefully containing phone numbers
    :rtype: list(string)
    :raise FileNotFoundError: if the file does not exist
    :raise OSError: if the file cannot be read
    """
    try:
        with open(file_path, mode='r') as file:
            rows = [row[0] for row in csv.reader(file)]
    except FileNotFoundError:
        raise FileNotFoundError("File not found: {0}".format(file_path))
    except OSError as os_e:
        raise OSError("An error occurred while reading the CSV file: {0}".format(os_e))

    return rows