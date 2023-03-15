class TV:
    def __init__(self):
        self._volume = 10
        self._max_volume = 100
        self._channel = 1
        self._channels = 150
        self._tv_on = False

    def turn_on_off(self):
        if self._tv_on is False:
            self._tv_on = True

        else:
            self._tv_on = False

    @property
    def volume(self):
        if self._tv_on is not True:
            return "The TV is off! Turn it on first!"
        else:
            return self._volume

    @volume.setter
    def volume(self, value):
        if 0 <= self._volume + value <= 100 and self._tv_on is True:
            self._volume += value
        elif self._tv_on is not True:
            print("Turn the TV on first!")

    @property
    def channel(self):
        if self._tv_on is not True:
            return "The TV is off! Turn it on first!"
        else:
            return self._channel

    @channel.setter
    def channel(self, chan):
        if 1 <= chan <= self._channels:
            self._channel = chan

    

if __name__ == "__main__":
    tv = TV()
    print(tv.volume)
    tv.turn_on_off()
    print(tv.volume)
    tv.volume = 25
    print(tv.volume)
    print(tv.channel)
    tv.channel = 141
    print(tv.channel)
    tv.channel = 200
    print(tv.channel)
    tv.volume = 80
    print(tv.volume)