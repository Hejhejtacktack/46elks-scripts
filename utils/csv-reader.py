import csv


def read(file):
    rows = []

    try:
        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            next(csv_reader)

            index = 0
            for row in csv_reader:
                rows.append(row)

    except FileNotFoundError:
        raise FileNotFoundError("File not found: {0}".format(file))
    except OSError as os_error:
        raise OSError('Error at index {0} when reading {1} file: {2}'.format(index, file, os_error))

    return rows