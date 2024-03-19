# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
# Вимоги до завдання:

#     Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
#     Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. 
#     Якщо задана дата пізніша за поточну, результат має бути від'ємним.
#     У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
#     Для роботи з датами слід використовувати модуль datetime Python.


from datetime import datetime

date_and_time_now =datetime.now()
date_now=date_and_time_now.date()

def get_days_from_today(date):
    date_user=datetime.strptime(date, "%Y-%m-%d")
    days_difference=date_now.toordinal()-date_user.toordinal()
    difference = int(days_difference)
    # print (f"кількість днів між заданою датою і поточною датою {date_now}, складає {difference} днів") 
    return difference

# get_days_from_today ('2023-10-09')

print (f"кількість днів між заданою датою і поточною датою {date_now}, складає {get_days_from_today ('2025-12-09')} днів")


