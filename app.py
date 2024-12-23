import time
from contact import Contact

class App():

  def __init__(self):
    self.contact_list = []

  def contactAdd(self, contact):
    self.contact_list.append(contact)

  def getContact(self, name):
    for contact in self.contact_list:
      if contact.name == name:
        print(contact)

c = Contact("Adson", "999999", "", "aaaaa@gmail.com")
c.phoneUpdate('999999', '999999')
c.phoneAdd('84999999999')
p = Phonebook()
p.contactAdd(c)
p.getContact('Adson')

input()
        
