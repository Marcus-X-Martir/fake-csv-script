import random as r
from faker import Faker
import csv
import sys

fake = Faker()

def sanitize_string_to_dict(string):
    key_values_string = string.split(',')
    argument_dict = {}
    for i in key_values_string:
        if i.split('=')[1].isdigit():
            argument_dict[i.split('=')[0]] = int(i.split('=')[1])
        else:
            argument_dict[i.split('=')[0]] = i.split('=')[1]
    return argument_dict

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
                elif fieldname == 'email':
                    row[fieldname] = r.choice([fake.email().split('@')[0] + ["@gmail.com", "@outlook.com", "@proton.me"][i] for i in range(3)])
                    if kwargs[fieldname] == "gmail":
                        row[fieldname] = fake.email().split('@')[0] + "@gmail.com"
                    elif kwargs[fieldname] == "outlook.com":
                        row[fieldname] = fake.email().split('@')[0] + "@outlook.com"
                    elif kwargs[fieldname] == "proton":
                        row[fieldname] = fake.email().split('@')[0] + "@proton.me"
                elif fieldname == 'age':
                    row[fieldname] = r.randint(kwargs[fieldname][0], kwargs[fieldname][1])
                elif fieldname == 'address':
                    row[fieldname] = ' '.join(fake.address().split())
                elif fieldname == 'id':
                    if isinstance(kwargs[fieldname], int):
                        global unique_id_int
                        try:
                            row[fieldname] = unique_id
                            unique_id += 1
                        except NameError:
                            unique_id = 0
                            row[fieldname] = unique_id
                            unique_id += 1
            dict_writer.writerow(row)
            row = {}
            rows -= 1

#
# create_fake_csv() can take in the following arguements:
# REQUIRED:   rows={int value}; This will determine how many rows to write; Take note that an additional row will be added for the header.
# 1 REQUIRED:   id={int value}; The value holds no significance for now,
#               name={int value from 1 to 3 inclusive}; 1 = first name; 2 = first and last; 3 = first and last plus possible title,
#               age={list with 2 ints in the order of less to greater}; age[0] = minimum age; age[1] = maximum age,
#               email={int value}; The value holds no significance for now,
#               address={int value}; The value holds no significance for now.
# 

create_fake_csv(int(sys.argv[1]), **sanitize_string_to_dict(str(sys.argv[2])))
