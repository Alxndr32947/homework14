class House:
    def __init__(self, name, number_of_floors):
        """
        Инициализация объекта класса House.

        :param name: Название дома (строка)
        :param number_of_floors: Количество этажей (целое число)
        """
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Метод для перехода на указанный этаж.
        :param new_floor: Этаж, на который нужно перейти.
        """
        if 1 <= new_floor <= self.number_of_floors:
            print(*range(1, new_floor + 1), sep="\n")
        else:
            print("Такого этажа не существует")


# Пример использования
if __name__ == "__main__":
    house1 = House("ЖК Эльбрус", 30)
    house2 = House("Коттедж", 2)
    
    house1.go_to(5)  # Вывод этажей от 1 до 5
    house2.go_to(10)  # Сообщение о недопустимом этаже
