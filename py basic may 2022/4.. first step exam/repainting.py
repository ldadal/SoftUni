protection = 1.5
paint_per_litter = 14.5
separator_per_litter = 5
bin = 0.4
nylon = int(input())
paint = int(input())
separator = int(input())
hours = int(input())
price_nylon = (nylon + 2) * protection
price_paint = (paint + paint * 10 / 100) * paint_per_litter
price_separator = separator * separator_per_litter
total_sum_for_matterials = price_nylon + price_paint + price_separator + bin
sum_for_painter = total_sum_for_matterials * 30 / 100 * hours
total = total_sum_for_matterials + sum_for_painter
print(total)
