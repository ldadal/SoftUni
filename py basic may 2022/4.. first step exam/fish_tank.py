length = int(input())
width = int(input())
height = int(input())
percentage = float(input())
volume = length * width * height * 0.001
litters_watter = volume - volume * percentage / 100
print(litters_watter)