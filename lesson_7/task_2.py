# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
    # реализовать абстрактные классы для основных классов проекта,  --
    # проверить на практике работу декоратора @property.            -- вот эти 2 штуки только использованием абстрактного метода и проверил, получается


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_material(self) -> float:
        pass


class DataStorage:
    total_calculated_material = 0.0


class Coat(Clothes, DataStorage):
    def __init__(self, volume: float):
        self.volume = volume

    def calc_material(self) -> float:
        result = round(self.volume/6.5 + 0.5, 2)
        DataStorage.total_calculated_material += result
        return result


class Suit(Clothes, DataStorage):
    def __init__(self, height: float):
        self.height = height

    def calc_material(self) -> float:
        result = round(2 * self.height + 0.3, 2)
        DataStorage.total_calculated_material += result
        return result


init_material_list = [
    Coat(50),
    Coat(23),
    Coat(84),
    Suit(1.6),
    Suit(1.8),
    Suit(1.9)
]

for clothe in init_material_list:
    print(f'Перед подсчётом всего материала: {clothe.total_calculated_material}, расчётный материал: {clothe.calc_material()}, тотал материала: {clothe.total_calculated_material}')
