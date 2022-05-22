from faker import Faker
fake = Faker(['pl_PL'])

class people:
   def __init__(self, name, address):
       self.name = name
       self.address = address

list=[]

for _ in range(2):
    person = people(name = fake.name, address = fake.address)
    list.append(person)

for item in list:
    print(item.name, item.address, '\t')