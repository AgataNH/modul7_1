class people:
   def __init__(self, name, surname, adress):
       self.name = name
       self.surname = surname
       self.adress = adress

person1 = people(name ="aaaa", surname ="bbbb", adress = "ccccc ccccc")
person2 = people(name ="ffff", surname ="gg", adress = "hhhh ccccc")
person3 = people(name ="xxxx", surname ="ccc", adress = "vvv v")
list = (person1, person2, person3)
for item in list:
    print(item.name, item.surname, item.adress, '\t')