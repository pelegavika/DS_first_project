# Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання 
# і повторного використання вже обчислених значень чисел Фібоначчі.

# Вимоги до завдання:

#     Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
#     fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
#     Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
#     Використання рекурсії для обчислення чисел Фібоначчі.

def caching_fibonacci(n, cache={}):
    
    def fibonacci(n):
        
        if n <= 0:
            return 0
        elif n==1:
            return 1
        elif n in cache.keys():
            return cache[n]
        else:    
            rez= fibonacci(n - 1) + fibonacci(n - 2)
            cache[n]=rez
            return rez
         
    return fibonacci(n)    


fib0 = caching_fibonacci(0)
fibneg3 = caching_fibonacci(-3)

fib10 = caching_fibonacci(10)
fib8 = caching_fibonacci(8)
fib15 = caching_fibonacci(15)

print(fib0)  # Виведе 0
print(fibneg3)  # Виведе 0
print(fib10)  # Виведе 55
print(fib8)  # Виведе 21
print(fib15)  # Виведе 610


