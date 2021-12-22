# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from random import choice

class Stock:
    printers = 0
    scanners = 0
    copy_machine = 0

    def __str__(self):
        return f'Printers - {self.printers}, Scanners - {self.scanners}, Copy machine - {self.copy_machine}'

class OfficeTech(Stock):

    def __init__(self, printer=False, scanner=False, copy_machine=False):
        if printer:
            Stock.printers += 1
        elif scanner:
            Stock.scanners += 1
        elif copy_machine:
            Stock.copy_machine += 1


class Printer(OfficeTech):
    def __init__(self):
        super().__init__(printer=True)

class Scanner(OfficeTech):
    def __init__(self):
        super().__init__(scanner=True)

class CopyMachine(OfficeTech):
    def __init__(self):
        super().__init__(copy_machine=True)


obj_list = []
for obj in range(1, 101):
    obj_list.append(choice([Printer, Scanner, CopyMachine])())

print(Stock())


