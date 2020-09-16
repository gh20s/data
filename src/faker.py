from faker import Faker
fake = Faker()
fake_ca = Faker('en_CA')

for _ in range(10):
    print(fake.company())
    print(fake_ca.address())
