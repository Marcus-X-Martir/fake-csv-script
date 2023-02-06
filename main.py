import random as r
from faker import Faker

def create_randint_list(k, low=0, high=99):
    return [r.randint(low, high) for i in range(k)]

fake = Faker()

def create_fake_csv(**kwargs):
    pass
