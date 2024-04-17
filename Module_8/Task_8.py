from collections import UserDict
from datetime import datetime, timedelta
import pickle

class DataFormatException(Exception):
    pass


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
            raise DataFormatException ('Give me name please.')
    

class Phone(Field): 
    def __init__(self, value):

        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise DataFormatException ('The Phone Number is incorrect')
        


class Birthday(Field):
    def __init__(self, value):
        try:
            dob=datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(dob)
        except ValueError:
            raise DataFormatException ("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

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
        


    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

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
        


def input_error(func):
    
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DataFormatException as err:
            return err
        except ValueError:
            return "Give me name and phone please."  
        except IndexError:
            return "Give me name please." 
        except KeyError:
            return "Name not found."     
    return inner



def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено




def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def find_next_weekday (d, weekday: int):  # Функція для знаходження наступного заданого дня тижня після заданої дати
    days_ahead = weekday - d.weekday()  # Різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <=0:  # Якщо день народження вже минув
        days_ahead += 7  # Додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  # Повертаємо нову дату 


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        message = "Contact not found."
    else:
        return f"Record found: {record}"
    return message
      
@input_error
def change_contact (args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        message = "Contact not found."
    else:
        if len(record.phones) > 0:
            record.phones[0]=Phone(phone)
        else:
            record.add_phone(phone)
    return message



@input_error
def add_birthday(args, book):
    name, dob = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        message = "Contact not found."
    else:
        record.birthday=Birthday(dob)
    return message 

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    else:
        return f"Birthday is: {record.birthday}"
    

def birthdays(book):
    days = 7 
    today = datetime.today().date()  
    birthdays_to_select = []  # Список майбутніх днів народження
    

    for record in book.data.items():
        contact=record[1]
        birthday_this_year=contact.birthday.value.replace(year=today.year) 
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        elif 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
            congratulation_date_str = birthday_this_year.strftime("%d.%m.%Y")
            birthdays_to_select.append({
                "contact": str(contact),
                "congratulation_date": congratulation_date_str
            })
    if len(birthdays_to_select)==0:
        return "There are no upcomming birthdays next week"

    return birthdays_to_select


def show_all (book: AddressBook):
    massage=""
    for record in book.data.items():
        massage+=str(record)+"\n"
    return massage

def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
           print(add_birthday(args, book))

        elif command == "show-birthday":
             print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")
            pass



if __name__ == "__main__":
    main()

