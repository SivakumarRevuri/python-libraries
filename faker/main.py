from faker import Faker

def generate_fake_data(count: int):
    fake = Faker()
    for _ in range(count):
        person_name = fake.name()
        person_gender = fake.random_element(elements={'male', 'female', 'others'})
        person_address = fake.city()
        person_dob = fake.date()
        person_email = fake.email()
        print(person_name, person_gender, person_email, person_dob, person_address)
    

while True:
    no_fake = input("Please enter how many Fake profiles you want to generate: ")
    if no_fake.isdigit():
        generate_fake_data(int(no_fake))
        break
    else:
        print('please enter a valid input')