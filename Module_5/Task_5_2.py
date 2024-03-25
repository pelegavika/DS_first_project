# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа,
# що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, 
# чітко відокремлені пробілами з обох боків. 
# Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел 
# і обчислення загального прибутку.

# Вимоги до завдання:

# 1 Функція generator_numbers(text: str) повинна приймати рядок як аргумент 
# і повертати генератор, що ітерує по всіх дійсних числах у тексті. 
# Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
# 2 Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers 
# для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.


from typing import Callable 
import re
from decimal import Decimal
def generator_numbers(some_text: str):
    num_list = re.findall(r'(\d+\.\d+)', some_text)
    # print(num_list)
    n=1
    while n <=len(num_list):
        for i in num_list:
            num= Decimal(i)
            yield num
            n+=1       
    

def sum_profit (text: str, func ):
    iterator = iter(func(text))
    sum=Decimal("0")
    next_element_exist=True
    while next_element_exist:
        try:
            sum+=next(iterator)
                    
        except StopIteration:
            next_element_exist = False 
    return sum
   

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, \
доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

