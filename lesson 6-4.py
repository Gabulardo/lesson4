class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} находится в движении.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nСкорость автомобиля {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревышаете!!! Ваша скорость {self.speed}!!!'
        else:
            return f'\nВаша скорость {self.speed}! Спасибо!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревышаете!!! Ваша скорость {self.speed}!!!'
        else:
            return f'\nВаша скорость {self.speed}! Спасибо!'


class PoliceCar(Car):
    pass


town = TownCar('Renault', 65, 'red', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('направо'), town.stop())

sport = SportCar('Bugatti', 370, 'blue', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('GAZ', 25, 'white', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Ford', 60, 'black&white', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('налево'), police.stop())
