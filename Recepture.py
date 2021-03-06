cook_book = {
      'яйчница': [
        {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
        ],
      'стейк': [
        {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
        {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
        ],
      'салат': [
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
        ]
      }

# 1. Открываем файл
# 2. читаем построчно в цикле 
# 2. Читаем построчно без цикла, доходим до количества ингридиентов и включается цикл
# 3. Присваиваем переменным значения взятые из файла
# 4. Формируем новый словарь cook_book



global_spisok = []

def recepture_funct(number_of_ingredients):
    for x in range(number_of_ingredients):
        recepture_lists = f.readline().split("|")
        return global_spisok.append(recepture_lists)



with open("Recepture.txt") as f:
    for line in f:
        recepture = line
        number_of_ingredients = int(f.readline())

        #print(recepture_funct(number_of_ingredients))



    print("Рецепты закончились :( ")
#        recepture_lists = f.readline()
#        print(recepture, type(recepture))
#        print(number_of_ingredients, type(number_of_ingredients))
#        print(recepture_lists, type(recepture_lists))
#        if number_of_ingredients == 2:
#            recepture_lists = f.readline()
#            recepture_list = recepture_lists.split('|')
#        print(recepture_list)
#            #number_of_ingredients -= 1
#        break

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                                shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()
