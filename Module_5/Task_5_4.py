# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

# Вимоги до завдання:

# 1 Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
# Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# 2 Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. 
# Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.



def input_error(func):
    
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."  
        except IndexError:
            return "Give me name please." 
        except KeyError:
            return "Name not found."     
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return "This Name Is Exists \
                \r\nTo view records, enter the command ALL."
    else:
        contacts[name] = phone       
        return "Contact added."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
    
      
@input_error
def change_contact (args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone       
        return "Contact updated."


def show_all (contacts):
    return contacts



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command (close, exit, hello, add, change, phone, all): ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone (args, contacts))    
        elif command == "all":
            print(show_all (contacts))        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()