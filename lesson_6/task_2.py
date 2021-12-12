# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    __length_meters = 0
    __width_meters = 0

    def __init__(self, lenght: float, width: float):
        self.__length = lenght
        self.__width = width

    def get_road_raw_materials_vol(self, asphalt_sq_m_vol_by_one_cm_in_kg: float, road_depth_in_cm: float) -> tuple:

        kgs = self.__length * self.__width * asphalt_sq_m_vol_by_one_cm_in_kg * road_depth_in_cm

        tonnas = round(kgs/1000, 2)

        return kgs, ' - в килограммах', tonnas, ' - в тоннах'

kerchinskiy_bridge = Road(19_000, 23.1)
print(kerchinskiy_bridge.get_road_raw_materials_vol(25, 30))