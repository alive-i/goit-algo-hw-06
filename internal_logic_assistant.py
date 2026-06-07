from collections import UserDict


class Field():
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def validation_phone(phone: str) -> bool:
        return len(phone) == 10 and phone.isdigit()     


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        if Phone.validation_phone(phone):
            self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
            self.phones = [ph for ph in self.phones if ph.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        user_phone = self.find_phone(old_phone)
        if isinstance(user_phone, Phone) and Phone.validation_phone(new_phone):
            user_phone.value = new_phone
        else:
            raise ValueError("You entered incorrect data!")

    def find_phone(self, phone: str) -> Phone:
        return next((ph for ph in self.phones if ph.value == phone), None)
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)        

    def delete(self, name: str):
        self.data.pop(name, None)

    def __str__(self):
        name_width = max((len(name) for name in self.data), default=0) + 8 
        phone_width = max((len(record.phones) for record in self.data.values()), default=0)
        phone_width = phone_width * 10 + (phone_width - 1) * 2 + 10
        header_1 = f"|{"Address Book":^{name_width + phone_width + 1}}|"
        header_2 = f"|{"Name":^{name_width}}|{"Phones":^{phone_width}}|"
        separator = "-" * len(header_2)
        phone_book = ""
        for name, record in self.data.items():
            ph = f"{'; '.join(phone.value for phone in record.phones)}"
            phone_book += f"|{name:^{name_width}}|{ph:^{phone_width}}|\n{separator}\n"
        return "\n".join([separator, header_1, separator, header_2, separator, phone_book.rstrip("\n")])

