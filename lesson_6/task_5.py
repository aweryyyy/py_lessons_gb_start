# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки для {type(self)} (ручка) {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки для {type(self)} (карандаш) {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки для {type(self)} (маркер) {self.title}'

stationery_list = [
    Pen('красный карандаш'),
    Pencil('синяя ручка'),
    Handle('белый маркер')
]

for object in stationery_list:
    print(object.draw())