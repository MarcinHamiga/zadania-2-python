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