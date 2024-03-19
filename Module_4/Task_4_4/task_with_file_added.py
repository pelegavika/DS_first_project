# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, 
# та буде відповідати відповідно до введеної команди.
# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, 
# змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. 
# Щоб реалізувати таку нескладну логіку, скористаємося словником. 
# У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.


# Вимоги до завдання:

#     Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
#     Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. 
#      Команди та аргументи мають бути розпізнані незалежно від регістру введення.
#     Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. 
#      В разі введення команди "exit" або "close", програма повинна завершувати виконання.
#     Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
#     Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
#     Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return "The name is repeated. This Name is already in the list."
    else:
        contacts[name] = phone
        write_file(contacts)
        return "Contact added."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return contacts.get(name)
    else:
        return "Name not found."
      

def change_contact (args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        write_file(contacts)
        return "Contact updated."
    else:
        return "Name not found."
    
def show_all (contacts):
    return contacts

def write_file(contacts):
    with open('Module_4/Task_4_4/contacts.txt', 'w') as fl:
        for i in contacts:
            fl.write(i + "," + contacts[i]+ '\n')

def read_file():
    data={}
    try:
        with open('Module_4/Task_4_4/contacts.txt', 'r', encoding='utf-8') as fl:
            for line in fl:
                items=line.strip('\n').split(',')
                key, values = items[0], items[1]
                data[key]=values
            return data
    except IOError as e:
        return data


def main():
    print("Welcome to the assistant bot!")
    contacts=read_file ()
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