chiken_menu = 10.35
fish_menu = 12.4
vegan_menu = 8.15
delivery = 2.5
numbers_chiken = int(input())
numbers_fish = int(input())
numbers_vegan = int(input())
total_without_desert = numbers_vegan * vegan_menu + numbers_fish * fish_menu + numbers_chiken * chiken_menu
total_plus_desert = total_without_desert + total_without_desert * 20 / 100
total_plus_delivery = total_plus_desert + delivery
print(total_plus_delivery)
