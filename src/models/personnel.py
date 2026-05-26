"""
Personnel Model
"""

import random
from dataclasses import dataclass
from faker import Faker


def first_name_and_gender(fake: Faker):
    """Generate a gender-specific first name and gender."""
    gender = 'M' if random.randint(0, 1) == 0 else 'F'
    first_name = fake.first_name_male() if gender == 'M' else fake.first_name_female()
    return {'gender': gender, 'first_name': first_name}


@dataclass
class Personnel:
    """Class representing a person."""

    dod_id: int
    first_name: str
    last_name: str
    gender: str

    def __init__(self, dod_id: int):
        self.faker = Faker()
        self.dod_id = dod_id
        name_and_gender = first_name_and_gender(self.faker)
        self.first_name = name_and_gender['first_name']
        self.gender = name_and_gender['gender']
        self.last_name = self.faker.last_name()
