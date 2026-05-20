import random

from dataclass_csv import DataclassWriter
from faker import Faker
from src.models.personnel import Personnel
from src.models.address import Address

if __name__ == '__main__':
    faker = Faker()
    # Set seed values for Faker and random instances
    Faker.seed(0)
    random.seed(0)

    personnel = []
    addresses = []

    for i in range(100000):
        dod_id = faker.unique.ssn().replace('-','')
        person = Personnel(dod_id)
        personnel.append(person)
        address = Address(dod_id)
        addresses.append(address)

    with open("users.csv", "w") as f:
        w = DataclassWriter(f, personnel, Personnel)
        w.write()

    with open("addresses.csv", "w") as f:
        w = DataclassWriter(f, addresses, Address)
        w.write()
