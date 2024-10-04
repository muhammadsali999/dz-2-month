
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}, Damage: {self.damage}, Fly: {self.fly}"

    def catchphrase_length(self):
        return len(self.catchphrase)

    def true_phrase(self):
        return f"True in the {self.catchphrase}"


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.airborne_ability = "Can fly high"

    def double_health(self):
        super().double_health()  # Call the parent class method
        self.fly = True  # Ensures fly is True


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.earth_power = "Strong and sturdy"

    def double_health(self):
        super().double_health()  # Call the parent class method
        self.fly = True  # Ensures fly is True


class Villain(AirHero):  # Inheriting from AirHero
    people = 'monster'

    def gen_x(self):
        pass  # This method currently does nothing

    def crit(self):
        return self.damage ** 2  # Raising damage to the power of 2


# Создаем объекты новых классов
air_hero = AirHero("Peter Parker", "Spider-Man", "Web-slinging", 80, "With great power comes great responsibility!", 10)
earth_hero = EarthHero("Diana Prince", "Wonder Woman", "Super strength", 90, "I am Wonder Woman!", 15)

# Вызов новых методов
air_hero.double_health()
print(air_hero)  # Проверка состояния AirHero
print(air_hero.true_phrase())  # Проверка true_phrase

earth_hero.double_health()
print(earth_hero)  # Проверка состояния EarthHero
print(earth_hero.true_phrase())  # Проверка true_phrase

# Создаем объект Villain и применяем метод crit
villain = Villain("Lex Luthor", "Luthor", "Genius intellect", 70, "I will be the one to rule!", 20)
villain_damage = villain.crit()
print(f"Villain's crit damage: {villain_damage}")  # Вывод критического урона



