import csv
from faker import Faker


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

class RegistrationDataGenerator:
    def __init__(self):
        self.__fake = Faker("pl_PL")
        self.FIRST_NAME = self.__fake.first_name()
        self.LAST_NAME = self.__fake.last_name()
        self.POSTAL_CODE = self.__fake.postcode()