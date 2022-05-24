from faker import Faker
fake = Faker(['pl_PL'])

class BaseCard:
   def __init__(self, first_name, last_name, phone, email):
       self.first_name = first_name
       self.last_name = last_name
       self.phone = phone
       self.email = email

   def contact_1(self):
       return f'Wybieram numer {self.phone} i dzownię do {self.first_name} {self.last_name}'

   @property
   def namelength(self):
      return len(self.first_name + ' ' + self.last_name)

class BusinessCard(BaseCard):
   def __init__(self, company, job, office_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.company = company
       self.job = job
       self.office_phone = office_phone

   def contact_2(self):
       return f'Wybieram numer {self.office_phone} i dzownię do {self.first_name} {self.last_name}, pracującym jako {self.job}'

   @property
   def namelength(self):
      return len(self.first_name + ' ' + self.last_name)

def create_contacts(card_type, card_number):
    Card_list =[]
    for _ in range(card_number):
        person = BusinessCard(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email(), company = fake.company(), job = fake.job(), office_phone = fake.phone_number())
        Card_list.append(person)

    if card_type == 'Base':
        for item in Card_list:
            print(item.first_name, item.last_name, item.phone, item.email, '\t')
            print(item.namelength)
            print(item.contact_1())
    if card_type == 'Business':
        for item in Card_list:
            print(item.first_name, item.last_name, item.company, item.job, item.office_phone, '\t')
            print(item.namelength)
            print(item.contact_2())

create_contacts('Business', 2)