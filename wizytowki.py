from faker import Faker
fake = Faker(['pl_PL'])

class BaseCard:
   def __init__(self, first_name, last_name, phone, email):
       self.first_name = first_name
       self.last_name = last_name
       self.phone = phone
       self.email = email

   def contact(self):
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

   def contact(self):
       return f'Wybieram numer {self.office_phone} i dzownię do {self.first_name} {self.last_name}, pracującym jako {self.job}'

def create_contacts(card_type, card_number):
    card_list = []
    for _ in range(card_number):
        if card_type == 'Base':
            card = BaseCard(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email())
        elif card_type == 'Business':
            card = BusinessCard(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email(), company = fake.company(), job = fake.job(), office_phone = fake.phone_number())
        card_list.append(card)
    return card_list

for item in create_contacts('Business', 2):
    print(item.first_name, item.last_name, item.company, item.job, item.office_phone)
    print(item.namelength)
    print(item.contact(), '\n')
