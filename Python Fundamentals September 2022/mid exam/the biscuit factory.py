import math

worker_per_day = int(input())
count_workers = int(input())
biscuits_competing = int(input())
total_biscuits = 0
production_per_day = worker_per_day * count_workers

for day in range(1, 31):
    if day % 3 == 0:
        total_biscuits += math.floor(production_per_day - production_per_day * 25 / 100)
    else:
        total_biscuits += production_per_day
print(f"You have produced {total_biscuits} biscuits for the past month.")
dif = abs(total_biscuits-biscuits_competing)
percentage_dif = (dif / biscuits_competing) *100
if total_biscuits > biscuits_competing:
    print(f"You produce {percentage_dif:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage_dif:.2f} percent less biscuits.")
