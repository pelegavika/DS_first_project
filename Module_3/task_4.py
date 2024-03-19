# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
# Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, 
# яка допоможе вам визначати, кого з колег потрібно привітати.

# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про 
# ім'я користувача та його день народження. 
# Оскільки дні народження колег можуть припадати на вихідні, 
# ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

# Вимоги до завдання:
#     Параметр функції users - це список словників, де кожен словник містить ключі 
#     name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
#     Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. 
#     Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
#     Функція повертає список словників, де кожен словник містить інформацію про користувача 
#     (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alina Kots", "birthday": "1986.03.10"},
    {"name": "Roman Kotov", "birthday": "1992.03.14"},
]


def find_next_weekday (d, weekday: int):  # Функція для знаходження наступного заданого дня тижня після заданої дати
    """
     Ф-ція для знаходження наступного заданого дня тижня після заданої дати
    :param d: datetime.date - початкова дата
    :param weekday: int - день тижня від 0 (понеділок) до 6 (неділя)
    :return:
    """
    days_ahead = weekday - d.weekday()  # Різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <=0:  # Якщо день народження вже минув
        days_ahead += 7  # Додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  # Повертаємо нову дату



def get_users_list (users_list):
    prepared_users=[]
    for user in users:
        try:
            birthday=datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            prepared_users.append({"name": user["name"], "birthday": birthday})
        
        except ValueError:
            print(f"Некоректна дата народження для користувача {user["name"]}")
    return prepared_users


def get_upcoming_birthdays(birthdays_list) :
    days = 7 # Кількість днів для перевірки на наближені дні народження
    today = datetime.today().date()  # Поточна дата

    birthdays_to_select = []  # Список майбутніх днів народження
    birthdays_list=get_users_list(birthdays_list)
    # print(birthdays_list)
    
    for user in birthdays_list:  # Ітерація по підготовленим користувачам
        birthday_this_year=user["birthday"].replace(year=today.year)  # Заміна року на поточний для дня народження цього року
        if birthday_this_year < today:  # Якщо дата народження вже пройшла цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # Переносимо наступний рік
        elif 0 <= (birthday_this_year - today).days <= days:  # Якщо день народження в межах вказаного періоду
            if birthday_this_year.weekday() >= 5:  # Якщо день народження випадає на суботу або неділю
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  # Знаходимо наступний понеділок
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  # Форматуємо дату у рядок
            birthdays_to_select.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return birthdays_to_select


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

