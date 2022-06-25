import math

name = input()
money = float(input())
beers = int(input())
chips = int(input())
price_for_chips = beers * 1.2 * 0.45
total = math.ceil(price_for_chips*chips) + beers * 1.2
if total <= money:
    print(f"{name} bought a snack and has {(money-total):.2f} leva left.")
else:
    print(f"{name} needs {(total-money):.2f} more leva!")
