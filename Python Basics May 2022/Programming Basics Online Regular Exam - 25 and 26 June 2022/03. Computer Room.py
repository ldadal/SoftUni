month = input()
hours = int(input())
folks = int(input())
day_time = input()
price_for_hour = 0
if month == "march" or month=="april" or month=="may":
    if day_time == "day":
        price_for_hour = 10.5
    else:
        price_for_hour = 8.4
elif month == "june" or month=="july" or month=="august":
    if day_time == "day":
        price_for_hour = 12.6
    else:
        price_for_hour = 10.2
if folks >= 4:
    price_for_hour -= price_for_hour * 0.1
if hours >= 5:
    price_for_hour -= price_for_hour * 0.5
total = price_for_hour * folks * hours
print(f"Price per person for one hour: {price_for_hour:.2f}")
print(f"Total cost of the visit: {total:.2f}")
