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
    
def generate_dod_ids(count: int) -> list[int]:
    faker = Faker()
    dod_ids = set()

    while len(dod_ids) < count:
        dod_id = faker.unique.ssn().replace('-', '')
        dod_ids.add(dod_id)

    return list(dod_ids)

def generate_personnel_records(dod_ids: list[int]) -> list[Personnel]:
    personnel = []

    for id in dod_ids:
        personnel.append(Personnel(id))

    return personnel

def generate_address_records(dod_ids: list[int]) -> list[Address]:
    addresses = []

    for id in dod_ids:
        addresses.append(Address(id))

    return addresses

def write_csv(filename: str, records: list, record_type: type) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        writer = DataclassWriter(f, records, record_type)
        writer.write()

def main() -> None:
    initialize_random_seed()

    dod_ids = generate_dod_ids(100000)
    personnel = generate_personnel_records(dod_ids)
    addresses = generate_address_records(dod_ids)

    write_csv("users.csv", personnel, Personnel)
    write_csv("addresses.csv", addresses, Address)

if __name__ == '__main__':
    main()
