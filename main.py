from faker import Faker
import random
import csv

def first_name_and_gender(fake: Faker):
    g = 'M' if random.randint(0, 1) == 0 else 'F'
    n = fake.first_name_male() if g == 'M' else fake.first_name_female()
    return {'gender': g, 'first_name': n}

def address_information(fake: Faker):
    address = {'street_address': fake.street_address(), 'city': fake.city(), 'state': faker.state_abbr(), 'zipcode': fake.postcode(),
               'country': fake.current_country(), 'country_code': fake.current_country_code()}
    return address

if __name__ == '__main__':
    faker = Faker()
    Faker.seed(0)
    random.seed(0)
    with open('./personnel.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ssn', 'first_name', 'last_name', 'gender'])
        for i in range(100000):
            dod_id = faker.unique.ssn().replace('-','')
            n_g = first_name_and_gender(faker)
            last_name = faker.last_name()
            writer.writerow([dod_id, n_g['first_name'], last_name, n_g['gender']])
        print(address_information(faker))
