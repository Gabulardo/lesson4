class Road:
# Константа веса 25 килограмм
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self.weight_constanta = 25
        self.height = height
#Высота асфальта дополнительно переводится в метры путем деления на 100
    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight_constanta * (self.height / 100) / 1000
        print(f'Для покрытия всего дорожного полотна необходимо {round(asphalt_mass)} тонн асфальта')

r = Road(
    int(input('Введите длину асфальта в метрах: ')),
    int(input('Введите ширину асфальта в метрах: ')),
    int(input('Введите высоту асфальта в сантиметрах: ')),
)
r.asphalt_mass()
