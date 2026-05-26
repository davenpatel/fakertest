"""
Generate synthetic personnel and address CSV files.
"""

import random

from dataclass_csv import DataclassWriter
from faker import Faker
from src.models import Address, Personnel


def initialize_random_seed(seed: int = 0) -> None:
    """
    Sets the Faker and random seed values to ensure reproducibility of the generated data.
    This is crucial for testing and debugging, as it allows us to generate the same set of
    data across different runs of the program.
    """

    Faker.seed(seed)
    random.seed(seed)


def generate_dod_ids(count: int) -> list[int]:
    """
    Generates a specified number of unique DoD IDs using the Faker library. The DoD ID is created
    by generating a unique Social Security Number (SSN) and removing the dashes. The generated
    DoD IDs are stored in a set to ensure uniqueness, and the function continues to generate
    IDs until the desired count is reached. Finally, the unique DoD IDs are returned as a list.
    """

    faker = Faker()
    dod_ids = set()

    while len(dod_ids) < count:
        dod_id = int(faker.unique.ssn().replace('-', ''))
        dod_ids.add(dod_id)

    return list(dod_ids)


def generate_personnel_records(dod_ids: list[int]) -> list[Personnel]:
    """
    Generates personnel records based on a list of DoD IDs. For each DoD ID, a Personnel
    object is created and initialized with the DoD ID. The generated Personnel records are
    collected in a list and returned at the end of the function. This allows us to create
    a structured dataset of personnel information that can be easily written to a CSV file
    or used for further processing.
    """

    personnel = []

    for dod_id in dod_ids:
        personnel.append(Personnel(dod_id))

    return personnel


def generate_address_records(dod_ids: list[int]) -> list[Address]:
    """
    Generates address records based on a list of DoD IDs. Similar to the personnel records,
    for each DoD ID, an Address object is created and initialized with the DoD ID.
    The generated Address records are collected in a list and returned at the end of
    the function. This allows us to create a structured dataset of address information
    that can be easily written to a CSV file or used for further processing.
    """

    addresses = []

    for dod_id in dod_ids:
        addresses.append(Address(dod_id))

    return addresses


def write_csv(filename: str, records: list, record_type: type) -> None:
    """
    Writes a list of records to a CSV file using the DataclassWriter from the dataclass_csv
    library. The function takes the filename, the list of records, and the type of the
    records as parameters. It opens the specified file in write mode with UTF-8 encoding,
    creates a DataclassWriter instance with the file, records, and record type, and then
    calls the write method to output the data to the CSV file. This function abstracts away
    the details of writing to a CSV file and allows for easy reuse when writing different
    types of records.
    """

    with open(filename, "w", encoding="utf-8") as f:
        writer = DataclassWriter(f, records, record_type)
        writer.write()


def main() -> None:
    """
    The main function serves as the entry point of the program. It initializes the random seed for
    reproducibility, generates a specified number of unique DoD IDs, creates personnel and address
    records based on those IDs, and finally writes the generated records to CSV files. This function
    orchestrates the entire data generation process and ensures that all steps are executed in the
    correct order. By calling the main function when the script is run, we can easily generate the
    desired datasets with a single command.
    """

    initialize_random_seed()

    dod_ids = generate_dod_ids(100000)
    personnel = generate_personnel_records(dod_ids)
    addresses = generate_address_records(dod_ids)

    write_csv("users.csv", personnel, Personnel)
    write_csv("addresses.csv", addresses, Address)


if __name__ == '__main__':
    main()
