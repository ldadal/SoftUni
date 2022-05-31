from math import pi

figure = input()
first_input = float(input())
result = 0
if figure == "circle" or figure == "square":
    if figure == "circle":
        result = first_input ** 2 * pi
    else:
        result = first_input * first_input
else:
    second_input = float(input())
    if figure == "rectangle":
        result = first_input * second_input
    else:
        result = first_input * second_input / 2
print(f"{result:.3f}")
