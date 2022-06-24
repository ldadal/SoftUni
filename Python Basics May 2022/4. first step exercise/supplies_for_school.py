pens = 5.8
markers = 7.2
washer = 1.2
packeges_pens = int(input())
packeges_markers = int(input())
litters_washer = int(input())
discound = float(input())
total_cost = packeges_markers * markers + packeges_pens * pens + litters_washer * washer
total_after_dicound = total_cost - (total_cost * discound / 100)
print(total_after_dicound)