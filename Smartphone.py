import pickle as pck

class Smartphone:
    def __init__(self):
        self.__manufacturer = None
        self.__model = None
        self.__price = None

    def set_manufacturer(self, manu: str) -> None:
        self.__manufacturer = manu

    def set_model(self, model: str) -> None:
        self.__model = model

    def set_price(self, price: int) -> int:
        if not isinstance(price, int):
            try:
                price = int(price)
            except ValueError:
                return -1
        self.__price = price
        return 1

    def print_manufacturer(self):
        print(self.__manufacturer)

    def print_model(self):
        print(self.__model)

    def print_price(self):
        print(self.__price)

    def __str__(self):
        return f"Model: {self.__model}; Manufacturer: {self.__manufacturer}; Price: {self.__price}"

    
if __name__ == "__main__":
    phone1, phone2 = Smartphone(), Smartphone()
    
    phone1.set_manufacturer("Samsung")
    phone1.set_model("S23")
    phone1.set_price(5499)

    phone2.set_manufacturer("Xiaomi")
    phone2.set_model("Mi 12")
    phone2.set_price(4999)

    print(phone1)
    print(phone2)

    with open("phones.dat", "wb") as file:
        pck.dump(phone1, file)
        pck.dump(phone2, file)

    with open("phones.dat", "rb") as file:
        phone3 = pck.load(file)
        phone4 = pck.load(file)

    print(phone3)
    print(phone4)