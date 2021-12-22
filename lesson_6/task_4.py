# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0.0
    color = ''
    name = ''
    is_police = False

    # protected parameters
    _car_moving = False
    _max_speed = 0.0

    def __init__(self, speed: float, color: str, name: str, is_police=False):
        self._max_speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed: float) -> str:
        self._car_moving = True
        self.speed = speed if speed <= self._max_speed else self._max_speed
        return f'{self.name} - поехала'

    def stop(self) -> str:
        self._car_moving = False
        self.speed = 0.0
        return f'{self.name} - остановилась'

    def turn(self, direction: str) -> str:
        return f'{self.name} - повернула {direction}'

    def show_speed(self) -> str:
        return str(self.speed)


class TownCar(Car):
    def show_speed(self) -> str:
        if self.speed > 60.0:
            return f'{self.speed} Превышение скорости, максимум - {60}'
        else:
            return str(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self) -> str:
        if self.speed > 40.0:
            return f'{self.speed} Превышение скорости, максимум - {40}'
        else:
            return str(self.speed)


class PoliceCar(Car):
    pass

cars_in_town = [PoliceCar(speed=180, color='white/black', name='JonnyCar', is_police=True),
                SportCar(speed=240, color='blue', name='Jaguar'),
                TownCar(speed=120, color='pink', name='Kia'),
                WorkCar(speed=90, color='gray', name='Sprinter')]

from random import choice, randint

turn_direction = [
    'left', 'right', 'turn around'
]

for car in cars_in_town:
    speed = randint(30, 200)

    print(f'Начинаем движение со скоростью - {speed}')
    print(car.go(speed))
    print(car.show_speed())
    print(car.turn(choice(turn_direction)))
    print(f'Speed - {car.speed}, Color - {car.color}, Name - {car.name}, Is police - {car.is_police}')
    print(car.stop())
    print(f'Speed - {car.speed}')
    print('\n\n')