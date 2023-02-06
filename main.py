import random as r
from faker import Faker
import csv

def create_randint_list(k, low=0, high=99):
    return [r.randint(low, high) for i in range(k)]

fake = Faker()

def create_fake_csv(**kwargs):
    fieldnames = []
    for key, value in kwargs.items():
        print('{key}: {value}'.format(key=key, value=value))
        fieldnames.append(key)
    with open('fake.csv', 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
        dict_writer.writerow()

create_fake_csv(name='Marcus', age=17)
