class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}"

    def catchphrase_length(self):
        return len(self.catchphrase)


# Создаем объект класса SuperHero
hero = SuperHero("Clark Kent", "Superman", "Flight", 100, "Up, up, and away!")

# Применяем методы
print(hero.get_name())  # Имя героя
hero.double_health()  # Умножаем здоровье на 2
print(hero.health_points)  # Текущее здоровье
print(hero)  # Строковое представление героя
print(hero.catchphrase_length())  # Длина коронной фразы