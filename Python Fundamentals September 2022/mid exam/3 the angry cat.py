price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_items = input()
left_side = 0
right_side = 0

if type_of_items == "cheap":
    for x in price_ratings[:entry_point]:
        if price_ratings[entry_point] > x and left_side < price_ratings[x]:
            left_side += x
    for x in price_ratings[entry_point + 1:]:
        if price_ratings[entry_point] > x and right_side < price_ratings[x]:
            right_side += x
else:
    for x in price_ratings[:entry_point]:
        if price_ratings[entry_point] <= x:
            left_side += x
    for x in price_ratings[entry_point + 1:]:
        if price_ratings[entry_point] <= x:
            right_side += x

if left_side >= right_side:
    print(f"Left - {left_side}")
elif right_side > left_side:
    print(f"Right - {right_side}")
