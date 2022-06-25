import math

paint_boxes = int(input())
wallpaper_rolls = int(input())
gloves_price = float(input())
brush_price = float(input())
sum_for_paint = paint_boxes * 21.5
sum_for_wallpapers = wallpaper_rolls * 5.2
needed_gloves = math.ceil(wallpaper_rolls * 0.35)
needed_brushes = math.floor(paint_boxes * 0.48)
total = sum_for_paint + sum_for_wallpapers + needed_brushes * brush_price + needed_gloves * gloves_price
delivery = total / 15
print(f"This delivery will cost {delivery:.2f} lv.")
