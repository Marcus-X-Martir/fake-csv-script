import random as r
from faker import Faker
import csv

def create_randint_list(k, low=0, high=99):
    return [r.randint(low, high) for i in range(k)]

fake = Faker()

def create_fake_csv(rows, **kwargs):
    """ Pre-Conditions: Takes in keywords and uses the name of the keys as a guide to create a fake csv file
        Post-Condition: A fake csv file is created in the directory that the script is called in
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
                    if kwargs[fieldname] == 1:
                        row[fieldname] = fake.name().split()[0]
                    elif kwargs[fieldname] == 2:
                        row[fieldname] = ' '.join(fake.name().split()[:2])
                    elif kwargs[fieldname] == 3:
                        row[fieldname] = ' '.join(fake.name().split()[:3])
                    else:
                        raise(valueError)
                elif fieldname == 'email':
                    row[fieldname] = fake.email()
                elif fieldname == 'age':
                        row[fieldname] = r.randint(kwargs[fieldname][0], kwargs[fieldname][1])
            dict_writer.writerow(row)
            row = {}
            rows -= 1


create_fake_csv(5, name=3, age=[18, 99], email=1, )
