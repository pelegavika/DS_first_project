from collections import UserDict



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        cleaned_value= value.strip().lower().title()
        if len(cleaned_value) !=0:
           self.value= cleaned_value
        else:
            raise ValueError('Give me name please.')
    
class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('The Phone Number is incorrect')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        if self.find_phone(phone_number):
            raise ValueError('The Phone Number Already Exists')    
        self.phones.append(Phone(phone_number))      
        
      
    def remove_phone(self, phone_number):
        if not self.find_phone(phone_number):
            raise ValueError('The Phone Number Not Found')  
        self.phones = [p for p in self.phones if str(p) != phone_number]



    def edit_phone(self, phone_number, new_phone_number):
        if not self.find_phone(phone_number):
            raise ValueError('The Phone Number Not Found')

        if self.find_phone(new_phone_number):
            raise ValueError('The New Phone Number Already Exists')
        self.phones = [Phone(new_phone_number) if p.value==phone_number else p for p in self.phones]
      

    def find_phone(self, phone_number):
        for item in self.phones:
            if item.value == phone_number:
                return phone_number
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if self.data.get(record.name.value):
            raise ValueError('The Record Already Exists')    
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
       if not self.data.get(name):
            raise ValueError('The Record Not Found')
       del self.data[name]
        



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")


# Виведення всіх записів у книзі #2
for name, record in book.data.items():
    print(record)