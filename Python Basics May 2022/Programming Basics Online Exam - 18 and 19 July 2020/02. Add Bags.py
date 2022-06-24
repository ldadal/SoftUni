price = float(input())
luggage_weight = float(input())
left_days = int(input())
count_luggage = int(input())
if luggage_weight < 10:
    price = price * 0.2
elif luggage_weight >= 10 and luggage_weight <= 20:
    price = price * 0.5
if left_days < 7:
    price = price + price * 0.4
elif left_days >= 7 and left_days <= 30:
    price = price + price * 0.15
else:
    price = price + price * 0.1

print(f" The total price of bags is: {price*count_luggage:.2f} lv. ")
