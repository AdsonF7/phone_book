class Contact():
    
  def __init__(self, name, phone, address='', email=''):
    self._name = name
    self._phones = [phone]
    self._address  = address
    self._email = email

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, new_name):
    self._name = new_name

  @property
  def address(self):
    return self._address

  @address.setter
  def address(self, new_address):
    self._address = new_address

  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, new_email):
    self._email = new_email
    
  def phoneAdd(self, phone):
    if phone not in self._phones:
      self._phones.append(phone)
      return 'PHONE ADDED'
    raise 'PHONE ALREADY EXISTS'
  
  def phoneRemove(self, phone):
    if phone in self._phones:
      self._phones.remove(phone)
      return 'PHONE REMOVED'
    raise 'PHONE DOES NOT EXISTS'
  
  def phoneUpdate(self, old_phone, new_phone):
    if old_phone in self._phones:
      self._phones[self._phones.index(old_phone)] = new_phone
      return 'UPDATE PHONE'
    raise 'OLD PHONE DOES NOT EXISTS'
  
  def update(self, name, address='', email=''):
    if name != '':
      self.name = name
    if address != self.address:    
      self.address = address
    if email != self.email:
      self.email = email

  def __repr__(self):
    phones = "\n|  ".join(self._phones)
    return f'| Name: {self.name}\n| Phones:\n|  {phones}\n| Address: {self.address}\n| Email: {self.email}'
  

