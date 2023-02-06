import random as r
from faker import Faker
import csv

def create_randint_list(k, low=0, high=99):
    return [r.randint(low, high) for i in range(k)]

fake = Faker()

def create_fake_csv(rows, **kwargs):
    """ Pre-Conditions: Takes in keywords and uses the type(value) of the keys as a guide to create a fake csv file
        Post-Condition: A fake csv file is created
    """
    fieldnames = []
    with open('fake.csv', 'w', newline='') as file:
        for key, value in kwargs.items():
            print('{key}: {value}'.format(key=key, value=value))
            fieldnames.append(key)
        dict_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
        dict_writer.writeheader()
        row = {}
        while rows > 0:
            for fieldname in fieldnames:
                if fieldname == 'name':
                    row[fieldname] = fake.name()
                elif fieldname == 'age':
                    row[fieldname] = 
            dict_writer.writerow(row)
            row = {}
            rows -= 1


create_fake_csv(3, name=9)
