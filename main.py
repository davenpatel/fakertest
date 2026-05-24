"""
Entry Class
"""

import random

from dataclass_csv import DataclassWriter
from faker import Faker
from src.models import Address, Personnel

def initialize_random_seed(seed: int = 0) -> None:
    Faker.seed(seed)
    random.seed(seed)

def generate_personnel_records(count: int) -> list[Personnel]:
    faker = Faker()
    personnel = []

    for _ in range(count):
        dod_id = faker.unique.ssn().replace('-', '')
        personnel.append(Personnel(dod_id))

    return personnel

def generate_address_records(count: int) -> list[Address]:
    faker = Faker()
    addresses = []

    for _ in range(count):
        dod_id = faker.unique.ssn().replace('-', '')
        addresses.append(Address(dod_id))

    return addresses


def write_csv(filename: str, records: list, record_type: type) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        writer = DataclassWriter(f, records, record_type)
        writer.write()

def main() -> None:
    initialize_random_seed()

    personnel = generate_personnel_records(100000)
    addresses = generate_address_records(100000)

    write_csv("users.csv", personnel, Personnel)
    write_csv("addresses.csv", addresses, Address)

if __name__ == '__main__':
    main()
