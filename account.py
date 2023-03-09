class Account:
    def __init__(self, balance):
        self.__balance = balance

    def pay(self, amount):
        self.__balance += amount

    def take(self, amount):
        if self.__balance - amount < 0:
            print("Not enough credit available!")
        else:
            self.__balance -= amount

    def __str__(self):
        return f"Stan konta: {self.__balance}"


if __name__ == "__main__":
    acc = Account(1000)
    print(acc)
    acc.pay(150)
    print(acc)
    acc.take(250)
    print(acc)