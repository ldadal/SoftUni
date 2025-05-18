clothes = [int(x) for x in input().split()]
rack = int(input())
rack_capacity = rack
count_rack = 1
while clothes:
    current_clothe = clothes.pop()
    if (rack-current_clothe) >= 0:
        rack-=current_clothe
    else:
        count_rack+=1
        rack=rack_capacity
        rack-=current_clothe

print(count_rack)

