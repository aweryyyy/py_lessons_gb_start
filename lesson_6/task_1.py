# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import perf_counter

class TrafficLight:

    _color = ''

    def __init__(self):
        self.start_time = perf_counter()
        self.running()

    def running(self):
        colors_dict = {
            'красный': 7.0,
            'желтый': 2.0,
            'зелёный': 4.0,
        }

        time_from_start = perf_counter() - self.start_time

        if time_from_start // sum(colors_dict.values()) > 0:
            time_from_start = sum(colors_dict.values())

        if 0.0 < time_from_start <= colors_dict['красный']:
            self._color = 'красный'
        elif colors_dict['красный'] < time_from_start <= colors_dict['красный'] + colors_dict['желтый']:
            self._color = 'желтый'
        elif colors_dict['красный'] + colors_dict['желтый'] < time_from_start <= sum(colors_dict.values()):
            self._color = 'зелёный'
        return self._color


from time import sleep

tree_light = TrafficLight()
print(tree_light.running())
sleep(7)
print(tree_light.running())
sleep(2)
print(tree_light.running())
sleep(1)
print(tree_light.running())
