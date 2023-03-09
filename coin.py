from random import randint

class Coin:
    def __init__(self):
        self.side = None

    def throw(self):
        self.side = randint(0 ,1)

    def __str__(self):
        if self.side == 0:
            return "Reszka"
        elif self.side == 1:
            return "Orzeł"
        else:
            return "Niezdefiniowane"

    def __eq__(self, comp):
        return self.side == comp



coins = [Coin() for coin in range(0, 3)] # 0 - 1zł, 1 - 2zł, 2 - 5zł
for coin in coins:
    orly = 0
    reszki = 0
    for x in range(15):
        coin.throw()
        if coin.side == 0:
            reszki += 1
        if coin.side == 1:
            orly += 1
        print(coin, end=' ')
    print(f"\nOrly: {orly}; Reszki: {reszki}\n")

wygrane = 0
przegrane = 0
for instance in range(100):
    saldo = 0
    while saldo < 20:
        for coin in coins:
            coin.throw()
        if coins[0] == 1:
            saldo += 1
        
        if coins[1] == 1:
            saldo += 2

        if coins[2] == 1:
            saldo += 5

        if saldo == 20:
            wygrane += 1
            print("Wygrana")

        if saldo > 20:
            przegrane += 1
            print("przegrana")
    
        print(f"Instancja: {instance}; Saldo: {saldo}, 1zł: {coins[0]}, 2zł: {coins[1]}, 5zł: {coins[2]} ")
print(f"Wygrane: {wygrane}")

    
