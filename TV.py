class TV:
    def __init__(self):
        self.__volume = 10
        self.__max_volume = 10
        self.__channel = 1
        self.__channels = 15
        self.__tv_on = False

    def turn_on_off(self):
        if self.__tv_on is False:
            self.__tv_on = True

        else:
            self.__tv_on = False