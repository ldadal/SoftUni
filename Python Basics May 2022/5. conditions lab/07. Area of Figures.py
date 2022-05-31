import math

figure = input()
size = float(input())
if figure == "circle" or figure == "square":
    if figure == "circle":
        print(size * size * math.pi)
    else:
        print(size * size)
else:
    side_b = float(input())
    if figure == "rectangle":
        print(size * side_b)
    else:
        print(size * side_b / 2)
