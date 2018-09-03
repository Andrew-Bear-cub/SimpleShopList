"""импортируем модуль shelve для сохранения данных в списке в файл, для последующего импорта после закрытия"""
import shelve
"""Объявим переменную all_lists для хранения всех списков покупок в массиве, откуда они будут извлекаться по индексу -
названию списка"""
all_lists = []
"""открываем файл lists_DB... (зачем это тут бляяяяяяя, я забыл, но пускай будет, потом разберусь)"""
db = shelve.open('lists_DB')
for any_list in all_lists:
    db[any_list.name] = any_list
db.close()

"""Класс для хранения списка покупок. В нем есть словарь с элементами списка, имя списка, переменная для хранения общей 
стоимости всех товаров в списке и методы для добавления элемента в список, удаления элемента из списка, сохранения 
списка и подсчета полной стоимости"""


class ShopList:
    # Конструктор класса. словарь с элементами списка, имя списка, переменная для хранения общей
    # стоимости всех товаров в списке
    def __init__(self, name='new list', total_cost=0):
        self.sl = {}
        self.name = name
        self.total_cost = total_cost

    # метод для добавления товара в список

    def add_good(self, name, amount, price):
        self.sl[name] = (amount, price)

    # метод для удаления товара из списка

    def delete_good(self, name):
        del self.sl[name]

    # метод для удаления всех товаров в списке

    def delete_all(self):
        self.sl = {}

    # метод для названия списка

    def set_name(self, name):
        self.name = name

    # метод для подсчета общей стоимости списка

    def calculate_total_cost(self):
        total_cost = 0
        for name in self.sl:
            total_cost += int(self.sl[name][0] * self.sl[name][1])
        self.total_cost = total_cost

    # метод для сохранения списка

    def save_list(self):
        all_lists.append(self)

    # метод для строкового представления списка, не знаю, будет ли использоваться в итоге, пока нужен только для
    # отладки через консоль

    def __str__(self):
        return_line = self.name + ':\n\n'
        for key in self.sl:
            return_line += '{0}: {1}, {2} руб.\n'.format(key, self.sl[key][0], self.sl[key][1])
        return_line += '\n\nИтого: \t' + str(self.total_cost) + ' руб.'
        return return_line

# Запуск отладки при запуске модуля как самостоятельной программы. Добавляет список и в консоль выводит его
# отформатированное строковое представление


if __name__ == '__main__':
    print('Вы запустили модуль как самостоятельный, выполняется прогон тестов:\n')
    new_shopList = ShopList()
    new_shopList.set_name('Пятерочка')
    new_shopList.add_good('мясо', 5, 250)
    new_shopList.add_good('зелень', 2, 15)
    new_shopList.add_good('конфеты', 3, 100)
    new_shopList.calculate_total_cost()
    new_shopList.save_list()

    db = shelve.open('lists_DB')
    for any_list in all_lists:
        db[any_list.name] = any_list

    print('Количество записей в файле БД: ', len(db))
    print('Список всех ключей: ', list(db.keys()), '\n')
    for key in db:
        print(db[key])
    db.close()
