class Bank:
    def __init__(self, name, balance):
        self._name = name  # защищенный атрибут
        self._balance = balance  # защищенный атрибут

    def moneyX(self):
        amount = float(input("Введите сумму для пополнения счета: "))
        self._balance += amount
        print(f"Ваш новый баланс: {self._balance}")

    def _kill(self):
        self._balance = 0
        print("Баланс обнулен.")

    def __jackpot(self):
        self._balance *= 10
        print(f"Ваш баланс после джекпота: {self._balance}")

    def _merge_balance(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"Баланс после объединения: {self._balance}")
        else:
            print("Неверный объект для объединения.")


if __name__ == "__main__":
    client1 = Bank("Alice", 1000)
    client2 = Bank("Bob", 500)

    client1.moneyX()
    client1._merge_balance(client2)
    client1._kill()

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Деление на ноль невозможно.")
        return self.value / other.value

if __name__ == "__main__":
    calc1 = Calculator(10)
    calc2 = Calculator(5)

    print(f"Сложение: {calc1 + calc2}")
    print(f"Вычитание: {calc1 - calc2}")
    print(f"Умножение: {calc1 * calc2}")
    print(f"Деление: {calc1 / calc2}")