from faker import Faker
fake = Faker(['pl_PL'])

class Card:
   def __init__(self, first_name, last_name, company, job, email):
       self.first_name = first_name
       self.last_name = last_name
       self.company = company
       self.job = job
       self.email = email

   def contact(self):
       print('Kontaktuję się z {} {}, pracującym jako {}, email: {}'.format(self.first_name, self.last_name, self.job, self.email))

   @property
   def namelength(self):
      return len(self.first_name + ' ' + self.last_name)

card_list=[]

for _ in range(5):
    person = Card(first_name = fake.first_name(), last_name = fake.last_name(), company = fake.company(), job = fake.job(), email = fake.email())
    card_list.append(person)

for item in card_list:
    print(item.first_name, item.last_name, item.company, item.job, item.email, '\t')
    print(item.namelength)

