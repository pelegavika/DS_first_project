# У вас є текстовий файл, який містить інформацію про котів. 
# Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл 
# та повертає список словників з інформацією про кожного кота.

# Вимоги до завдання:
#     Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
#     Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
#     Функція має повертати список словників, де кожен словник містить інформацію про одного кота.



def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as fl:
        keys=["id", "name", "age"]
        data_cats=[]
        cats_info=[]
       
        for line in fl:
            data_cats=line.strip().split(',')
            dict_cats=dict(zip(keys, data_cats))
            cats_info.append(dict_cats)
                     
        return cats_info
  

cats_info = get_cats_info("Module_4/cats_inform.txt")
print(cats_info)