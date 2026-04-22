import csv


def get_csv_data(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows

def get_sample_login_csv(filename):
    rows = get_csv_data(filename)
    return rows[0]