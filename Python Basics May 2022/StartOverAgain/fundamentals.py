# num = float(input())
# if num == 0:
#     print("zero")
# elif num > 0:
#     if num < 1:
#         print("small positive")
#     elif num > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# else:
#     if abs(num) < 1:
#         print("small negative")
#     elif abs(num) > 1000000:
#         print("large negative")
#     else:
#         print("negative")
# from re import search
from os.path import split

# One = int(input())
# Two = int(input())
# Three = int(input())
# max = One
# if One < Two:
#     max = Two
# if max < Three:
#     max = Three
# print(max)

# word = input()
# print(word[::-1])

# numbers = int(input())
# count = 0
# for i in range(numbers):
#     num = int(input())
#     if num % 2 != 0:
#         print(f"{num} is odd!")
#         break
#     count += 1
# if count == numbers:
#     print("All numbers are even.")

# while True:
#     num = float(input())
#     if num >= 1 and num <= 100:
#         print(f"The number {num} is between 1 and 100")
#         break

# budget = int(input())
# command = input()
# while command != "End":
#     price = int(command)
#     if price > budget:
#         print("You went in overdraft!")
#         break
#     budget -= price
#     command = input()
# if command =="End":
#     print("You bought everything needed.")

# num = int(input())
# for streight in range(num):
#     for j in range(streight+1):
#         print("*", end="")
#     print()
# for reversed in range(num-1,0, -1):
#     for g in range(reversed):
#         print("*", end="")
#     if reversed==1:
#         break
#     print()

# name = input()
# if name=="Johnny":
#     print("Hello, my love!")
# else:
#     print(f"Hello, {name}!")

# age = int(input())
# if age<=14:
#     print("drink toddy")
# elif age>14 and age<=18:
#     print("drink coke")
# elif age>18 and age<=21:
#     print("drink beer")
# else:
#     print("drink whisky")

# n = int(input())
# for i in range (n):
#     num = int(input())
#     if num == 88:
#         print("Hello")
#     elif num == 86:
#         print("How are you?")
#     elif num < 88 and num != 86:
#         print("GREAT!")
#     elif num > 88:
#         print("Bye.")


# divisor = int(input())
# boundary = int(input())
# N=0
# for i in range(boundary+1):
#     if i%divisor==0:
#         N=i
# print(N)

# NumOfOrders = int(input())
# total = 0
# for i in range(NumOfOrders):
#     ppc = float(input())
#     days = int(input())
#     cpd = int(input())
#     if ppc>=0.01 and ppc<=100 and days>=1 and days<=31 and cpd>=1 and cpd<=2000:
#         orderPrice = ppc*days*cpd
#         total+=orderPrice
#         print(f"The price for the coffee is: ${orderPrice:.2f}")
# print(f"Total: ${total:.2f}")

# num = int(input())
# for i in range(num):
#     text = input()
#     if '.' in text:
#         print(f"{text} is not pure!")
#     elif ',' in text:
#         print(f"{text} is not pure!")
#     elif '_' in text:
#         print(f"{text} is not pure!")
#     else:
#         print(f"{text} is pure.")

# while True:
#     text = input()
#     if text == "End":
#         break
#     elif text != "SoftUni":
#         for char in text:
#             print(f"{char}{char}", end='')
#         print()

# coffeeNeeded = 0
# while True:
#     event = input()
#     if event == "END":
#         break
#     if event.lower() in ["coding", "dog", "cat", "movie"]:
#         if event.islower():
#             coffeeNeeded += 1
#         else
#             coffeeNeeded += 2
# if coffeeNeeded > 5:
#     print("You need extra sleep")
# else:
#     print(coffeeNeeded)
# voldeCount = 0
# while True:
#     name = input()
#     if name == "Welcome!":
#         break
#     if name == "Voldemort":
#         voldeCount += 1
#         print("You must not speak of that name!")
#         break
#     count = 0
#     for char in name:
#         count += 1
#     if count < 5:
#         print(f"{name} goes to Gryffindor.")
#     elif count == 5:
#         print(f"{name} goes to Slytherin.")
#     elif count == 6:
#         print(f"{name} goes to Ravenclaw.")
#     elif count > 6:
#         print(f"{name} goes to Hufflepuff.")
# if voldeCount == 0:
#     print("Welcome to Hogwarts.")


# first = input()
# second = input()
# first_list = list(first)
# second_list = list(second)
# for i in range(len(first)):
#     if first_list[i]!=second_list[i]:
#           first_list[i]=second_list[i]
#           first = ''.join(first_list)
#           print(first)

# budget = float(input())
# PriceFlour = float(input())
# PriceEggs = PriceFlour * 0.75
# PriceMilk = PriceFlour * 1.25 / 4
# totalForOneBread = PriceFlour + PriceEggs + PriceMilk
# countOfBread = 0
# countOfEggs = 0
# while True:
#     if budget - totalForOneBread >= 0:
#         budget -= totalForOneBread
#         countOfBread += 1
#         countOfEggs += 3
#     else:
#         break
#     if countOfBread % 3 == 0:
#         countOfEggs -= (countOfBread - 2)
# print(f"You made {countOfBread} loaves of Easter bread! Now you have {countOfEggs} eggs and {budget:.2f}BGN left.")

# quantity_of_decorations = int(input())
# days_till_Christmas = int(input())
# ornament_set = 2
# tree_skirt = 5
# tree_garland = 3
# tree_lights = 15
# spirit = 0
# total = 0
# for days in range(1, days_till_Christmas+1):
#     if days % 11 == 0:
#         ornament_set += ornament_set
#         tree_lights += tree_lights
#         tree_garland += tree_garland
#         tree_skirt += tree_skirt
#     if days % 2 == 0:
#         total += ornament_set
#         spirit += 5
#     elif days % 3 == 0:
#         total += (tree_garland + tree_skirt)
#         spirit += (10 + 3)
#     elif days % 5 == 0:
#         total += tree_lights
#         spirit += 17
#     elif days % 3 == 0 and days % 5 == 0:
#         spirit += 30
#     elif days % 10 == 0:
#         spirit -= 20
#         total += tree_skirt + tree_garland + tree_lights
#     elif days == days_till_Christmas and days % 10 == 0:
#         spirit -= 30
# print(f"Total cost: {total}")
# print(f"Total spirit: {spirit}")

# quantity_of_decorations = int(input())
# days_till_Christmas = int(input())
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garland_price = 3
# tree_lights_price = 15
#
# ornament_set_points = 5
# tree_skirt_points = 3
# tree_garland_points = 10
# tree_lights_points = 17
#
# total_cost = 0
# total_spirit = 0
#
# for day in range(1, days_till_Christmas + 1):
#     if day % 11 == 0:
#         quantity_of_decorations += 2
#
#     if day % 2 == 0:
#         total_cost += quantity_of_decorations * ornament_set_price
#         total_spirit += ornament_set_points
#
#     if day % 3 == 0:
#         total_cost += quantity_of_decorations * (tree_skirt_price + tree_garland_price)
#         total_spirit += tree_skirt_points + tree_garland_points
#
#     if day % 5 == 0:
#         total_cost += quantity_of_decorations * tree_lights_price
#         total_spirit += tree_lights_points
#         if day % 3 == 0:
#             total_spirit += 30
#
#     if day % 10 == 0:
#         total_spirit -= 20
#         total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
#
#     if day == days_till_Christmas and day % 10 == 0:
#         total_spirit -= 30
#
# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {total_spirit}")

# num = int(input())
# listOfNums = []
# while num != 0:
#     current_num = num%10
#     num=num//10
#     listOfNums.append(current_num)
# listOfNums.sort(reverse=True)
# result = ''.join(map(str, map(int, listOfNums)))
# print(result)

# text = input()
# list_of_capitals = []
# for i in range(len(text)):
#     if text[i].isupper():
#         list_of_capitals.append(i)
# print(list_of_capitals)

# queue = input()
# list_of_animals = queue.split(", ")
# count = 0
# check = 0
# for animal in list_of_animals:
#     count += 1
#     if animal == "wolf":
#         if count + 1 >= len(list_of_animals):
#             print("Please go away and stop eating my sheep")
#             check += 1
#         else:
#             count = 0
# if check == 0:
#     print(f"Oi! Sheep number {count}! You are about to be eaten by a wolf!")

# queue = input().split(", ")
#
# # Find the position of the wolf
# wolf_position = queue.index("wolf")
#
# # Check if the wolf is at the end of the list
# if wolf_position == len(queue) - 1:
#     print("Please go away and stop eating my sheep")
# else:
#     sheep_position = len(queue) - wolf_position - 1
#     print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")

# text = input()
# text = text.lower()
# word = "water"
# count = text.count(word)
# word = "fish"
# count += text.count(word)
# word = "sun"
# count += text.count(word)
# word = "sand"
# count += text.count(word)
# print(count)

# text = input().lower()
# words = ["sand", "water", "fish", "sun"]
# count = sum(text.count(word) for word in words)
# print(count)

#
# name = input()
# if name == 'Johnny':
#     print("Hello, my love!")
# else:
#     print(f"Hello, {name}!")

# num_of_strings = int(input())
# chars = [',', '.', '_']
# for i in range(num_of_strings):
#     text = input()
#     if any(char in text for char in chars):
#         print(f"{text} is not pure!")
#         continue
#     print(f"{text} is pure.")
    # for char in chars:
    #     if char in text:
    #         print(f"{text} is not pure!")
    #         break
    # else:
    #     print(f"{text} is pure.")

# text = input()
# list = []
# while text != "End":
#     if text != "SoftUni":
#         for char in text:
#             list.append(char)
#             list.append(char)
#         result = ''.join(list)
#         print(result)
#     list = []
#     text = input()

# command = input()
# coffees = 0
# while command != "END":
#     if command in ["coding", "dog", "cat", "movie", "CODING", 'DOG', 'CAT', 'MOVIE']:
#         if command.isupper():
#             coffees += 2
#         else:
#             coffees += 1
#     command = input()
# if coffees > 5:
#     print("You need extra sleep")
# else:
#     print(coffees)

# name = input()
# while name != "Welcome!":
#     if name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#     else:
#         print(name, end=' ')
#         if len(name)<5:
#             print("goes to Gryffindor.")
#         elif len(name)==5:
#             print("goes to Slytherin.")
#         elif len(name)==6:
#             print("goes to Ravenclaw.")
#         elif len(name)>6:
#             print("goes to Hufflepuff.")
#         name = input()
# if name == "Welcome!":
#     print("Welcome to Hogwarts.")

# first = input()
# second = input()
# list = []
# for char in first:
#     list.append(char)
# for i in range(len(list)):
#     for char in second:
#         if char != list[i]:
#             list[i] = char
#             print(list)

# first = input()
# second = input()
# list = list(first)
#
# for i in range(len(list)):
#     if list[i] != second[i]:
#         list[i] = second[i]
#         print(''.join(list))

# budget = float(input())
# flour_price = float(input())
# eggs_price = flour_price * 0.75
# milk_price = flour_price + flour_price * 0.25
# total_per_bread = eggs_price + flour_price + milk_price * 0.25
# count_breads = 0
# count_eggs = 0
# while budget >= total_per_bread:
#     budget -= total_per_bread
#     count_breads += 1
#     count_eggs += 3
#     if count_breads % 3 == 0:
#         count_eggs -= count_breads - 2
# print(f"You made {count_breads} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")

# num = input()
# list_of_nums = []
# for i in range(len(num)):
#     list_of_nums.append(num[i])
# list_of_nums.sort(reverse=True)
# result = ''.join(list_of_nums)
# print(result)
#
# text = input()
# lisf_of_capital = []
# for i in range(len(text)):
#     if text[i].isupper():
#         lisf_of_capital.append(i)
# print(lisf_of_capital)

# animal = []
# animal = input().split(', ')
# count = 0
# for i in range(len(animal), 0, -1):
#     if animal[i - 1] == "wolf":
#         if i == len(animal):
#             print("Please go away and stop eating my sheep")
#         break
#     else:
#         count += 1
# if count > 0:
#     print(f"Oi! Sheep number {count}! You are about to be eaten by a wolf!")
#
# animals = input().split(", ")
# wolf_position = animals.index("wolf")
# if wolf_position == len(animals) - 1:
#     print("Please go away and stop eating my sheep")
# else
#     sheep_counts = len(animals) - wolf_position - 1
#     print(f"Oi! Sheep number {sheep_counts}! You are about to be eaten by a wolf!")

# text = input().lower()
# words = ["sand", "water", "fish", "sun"]
# count = 0
# for word in words:
#     count += text.count(word)
# print(count)