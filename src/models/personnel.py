import random
from dataclasses import dataclass
from faker import Faker

def first_name_and_gender(fake: Faker):
    g = 'M' if random.randint(0, 1) == 0 else 'F'
    n = fake.first_name_male() if g == 'M' else fake.first_name_female()
    return {'gender': g, 'first_name': n}

@dataclass
class Personnel:
    dod_id: int = None
    first_name: str = None
    last_name: str = None
    gender: str = None

    faker = Faker()

    def  __init__(self, dod_id: int):
        self.dod_id = dod_id
        n_g = first_name_and_gender(self.faker)
        self.first_name = n_g['first_name']
        self.gender = n_g['gender']
        self.last_name = self.faker.last_name()