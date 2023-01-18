from collections import UserDict


class AddressBook(UserDict):

    """Create adressbook"""

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, record):
        self.data.pop(record.name.value, None)

    def show_record(self):
        return self.data


class Record:

    """Creating and editing contacts"""

    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add(self, new_number):
        self.phones.append(new_number)

    def edit(self, old_number, new_number):
        if old_number in self.phones:
            self.phones.remove(old_number)
            self.phones.append(new_number)
        else:
            return f"Phone number {old_number} is not found. Please try again"

    def remove(self, old_number):
        if old_number in self.phones:
            self.phones.remove(old_number)
        else:
            return f"Phone number {old_number} is not found. Please try again"


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')

