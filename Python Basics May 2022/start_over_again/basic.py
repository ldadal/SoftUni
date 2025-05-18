# Read a number and print excellent if it is greater than or equal to 5.50.
# score = float(input())
# if score >= 5.50:
#     print ("Excellent!")
#
# Read two numbers from the console and print the greater of them.
# numOne = float(input())
# numTwo = float(input())
# if numOne > numTwo:
#     print(numOne)
# else:
#     print(numTwo)
# import math
# from asyncio.unix_events import can_use_pidfd
# from email.policy import default
#
# Read a number from the console and print whether it is odd or even.
# num=int(input())
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
# Compare passwords
#
# password = input()
# if password == "s3cr3t!P@ssw0rd":
#     print("Welcome")
# else:
#     print("Wrong password!")
#
# Read a number from the console and print whether it is a number between 100 and 200, a number greater than 200 or a number less than 100.
#
# num = int(input())
# if num < 100:
#     print("Less than 100")
# else:
#     if num <= 200:
#         print("Between 100 and 200")
#     else:
#         print("Greater than"
#               " 200")
#
# Figure area
# figure = input()
# value = 0
# if figure == "square":
#     side = float(input())
#     value = (side * side)
# else:
#     if figure == "rectangle":
#         sideA = float(input())
#         sideB = float(input())
#         value = (sideA * sideB)
#     else:
#         if figure == "circle":
#             radius = float(input())
#             value = (3.14159265359 * radius * radius)
#         else:
#             if figure == "triangle":
#                 side = float(input())
#                 height = float(input())
#                 value = (side * height / 2)
# if value != 0:
#     print(f"{value:.3f}")
# else:
#     print("Unknown figure")
#
# sport time
# timeOne = int(input())
# timeTwo = int(input())
# timeThree = int(input())
# totalTime = timeOne + timeTwo + timeThree
# print(f"{totalTime//60}:{totalTime%60:02d}")
#
# extra points
# startingPoints = int(input())
# if startingPoints <= 100:
#     bonusPoints = 5
# else:
#     if startingPoints <= 1000 and startingPoints > 100:
#         bonusPoints = startingPoints * 0.2
#     else:
#         bonusPoints = startingPoints * 0.1
# if startingPoints%2==0:
#     bonusPoints +=1
# else:
#     if startingPoints%10==5:
#         bonusPoints +=2
# print(bonusPoints)
# print(startingPoints+bonusPoints)
#
# h and m + 15
# hours = int(input())
# minutes = int(input())
# if minutes+15 >= 60:
#     hours += 1
#     minutes = (minutes+15) - 60
# else:
#     minutes += 15
# if hours == 24:
#     hours = 0
# print(f"{hours}:{minutes:02d}")
#
# toy stora
# excursionPrice = float(input())
# puzzles = int(input())
# dolls = int(input())
# bears = int(input())
# minions = int(input())
# trucks = int(input())
# toys = puzzles + dolls + bears + minions + trucks
# totalPrice = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
# if toys >= 50:
#     totalPrice = totalPrice * 0.75
# totalPrice = totalPrice * 0.9
# if totalPrice >= excursionPrice:
#     print(f"Yes! {totalPrice-excursionPrice:.2f} lv left.")
# else:
#     print(f"Not enough money! {excursionPrice-totalPrice:.2f} lv needed.")
#
# godzilla vs kong
#
# budget = float(input())
# statists = int(input())
# costumePrice = float(input())
# decorPrice = budget * 0.1
# if statists>150:
#     costumePrice = costumePrice * 0.9
# totalPrice = statists * costumePrice + decorPrice
# if totalPrice <= budget:
#     print("Action!")
#     print(f"Wingard starts filming with {budget-totalPrice:.2f} leva left.")
# else:
#     print("Not enough money!")
#     print(f"Wingard needs {totalPrice-budget:.2f} leva more.")
#
# world swimming record
# worldRecord = float(input())
# distance = float(input())
# timePerMeter = float(input())
# late = distance // 15
# letaTime = late * 12.5
# time = distance * timePerMeter + letaTime
# if time < worldRecord:
#     print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
# else:
#     print(f"No, he failed! He was {time-worldRecord:.2f} seconds slower.")
#
# shopping
# budget = float(input())
# videoCards = int(input())
# processors = int(input())
# ram = int(input())
# videoCardPrice = videoCards * 250
# processorPrice = videoCardPrice * 0.35 * processors
# ramPrice = videoCardPrice * 0.1 * ram
# totalPrice = videoCardPrice + processorPrice + ramPrice
# if videoCards > processors:
#     totalPrice = totalPrice * 0.85
# if totalPrice <= budget:
#     print(f"You have {budget-totalPrice:.2f} leva left!")
# else:
#     print(f"Not enough money! You need {totalPrice-budget:.2f} leva more!")
#
# Lunch break
# showName = input()
# episodeTime = int(input())
# breakTime = int(input())
# lunchTime = breakTime * 0.125
# relaxTime = breakTime * 0.25
# leftTime = breakTime - lunchTime - relaxTime
# if leftTime>=episodeTime:
#     print(f"You have enough time to watch {showName} and left with {math.ceil(episodeTime-leftTime):.0f} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {showName}, you need {math.ceil(episodeTime-leftTime):.0f} more minutes.")
#
# DAY OF THE WEEK
# day = int(input())
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Error")
#
# Workin day or weekend
# day = input()
# match day:
#     case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#         print("Working day")
#     case "Saturday" | "Sunday":
#         print("Weekend")
#     case _:
#         print("Error")
#
# age and sex
# age = float(input())
# sex = input()
# if age < 16:
#     if sex == "m":
#         print("Master")
#     else:
#         print("Miss")
# else:
#     if sex == "m":
#         print("Mr.")
#     else:
#         print("Ms.")
#
# animal type
# animal = input()
# match animal:
#     case "dog":
#         print("mammal")
#     case "crocodile" | "tortoise" | "snake":
#         print("reptile")
#     case _:
#         print("unknown")
#
# city = input()
# sales = float(input())
# if sales >= 0 and sales <= 500.0:
#     if city == "Sofia":
#         commission = 5
#     elif city == "Varna":
#         commission = 4.5
#     else:
#         commission = 5.5
# elif sales > 500 and sales <= 1000:
#     if city == "Sofia":
#         commission = 7
#     elif city == "Varna":
#         commission = 7.5
#     else:
#         commission = 8
# elif sales > 1000 and sales <= 10000:
#     if city == "Sofia":
#         commission = 8
#     elif city == "Varna":
#         commission = 10
#     else:
#         commission = 12
# else:
#     if city == "Sofia":
#         commission = 12
#     elif city == "Varna":
#         commission = 13
#     else:
#         commission = 14.5
# if sales > 0 and (city == "Sofia" or city == "Varna" or city == "Plovdiv"):
#     print(f"{sales * commission / 100:.2f}")
# else:
#     print("error")
#
# fruit = input()
# day = input()
# quantity = float(input())
# price = 0
# if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
# elif day == "Saturday" or day == "Sunday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
# if price != 0:
#     print(f"{price * quantity:.2f}")
# else:
#     print("error")
#
# numOfStudents = int(input())
# numOfLectures = int(input())
# additionalBonus = int(input())
# maxBonus = 0
# maxLectures = 0
# for i in range(numOfStudents):
#     attendance = int(input())
#     totalBonus = attendance / numOfLectures * (5 + additionalBonus)
#     if totalBonus > maxBonus:
#         maxBonus = totalBonus
#         maxLectures = attendance
# print(f"Max Bonus: {math.ceil(maxBonus)}.")
# print(f"The student has attended {maxLectures} lectures.")
#
# priceStrawberry = float(input())
# bananasQuantity = float(input())
# orangeQuantity = float(input())
# maliniQuantity = float(input())
# strawberryQuantity = float(input())
# priceMalini = priceStrawberry*0.5
# priceOrange = priceMalini*0.6
# priceBananas = priceMalini*0.2
# total = priceStrawberry*strawberryQuantity+priceMalini*maliniQuantity+priceBananas*bananasQuantity+priceOrange*orangeQuantity
# print(f"{total:.2f}")
#
# budget = float(input())
# sleepCount = int(input())
# pricePerNight = float(input())
# percentExtraSpent = int(input())/100
# if sleepCount > 7:
#     pricePerNight = pricePerNight * 0.95
# total = sleepCount*pricePerNight+budget*percentExtraSpent
# if total>budget:
#     print(f"{total-budget:.2f} leva needed")
# else:
#     print(f"Ivanovi will be left with {budget-total:.2f} leva after vacation.")
#
# budget = float(input())
# fuel = float(input())
# dayOfWeek = input()
# total = fuel * 2.1 + 100
# if dayOfWeek == "Sunday":
#     total = total * 0.8
# else:
#     total = total * 0.9
# if budget < total:
#     print(f"Not enough money! Money needed: {total-budget:.2f} lv.")
# else:
#     print(f"Safari time! Money left: {budget-total:.2f} lv.")
#
# srok = input()
# tip = input()
# internet = input()
# meseci = int(input())
# tax = 0
# netTax = 0
# total = 0
# if srok == "one":
#     match tip:
#         case "Small":
#             tax = 9.98
#         case "Middle":
#             tax = 18.99
#         case "Large":
#             tax = 25.98
#         case "ExtraLarge":
#             tax = 35.99
# else:
#     match tip:
#         case "Small":
#             tax = 8.58
#         case "Middle":
#             tax = 17.09
#         case "Large":
#             tax = 23.59
#         case "ExtraLarge":
#             tax = 31.79
# if internet == "yes":
#     if tax <= 10:
#         netTax = 5.5
#     elif tax > 10 and tax <= 30:
#         netTax = 4.35
#     else:
#         netTax = 3.85
# total = tax*meseci+netTax*meseci
# if srok == "two":
#     total = total*0.9625
# print(f"{total:.2f} lv.")
#
# budget = float(input())
# productName = input()
# price = float(input())
# count = 1
# total = price
# budget -= price
# while productName != "Stop":
#     productName = input()
#     if productName == "Stop":
#         print(f"You bought {count} products for {total:.2f} leva.")
#         break
#     price = float(input())
#     count += 1
#     if count % 3 == 0:
#         price = price * 0.5
#     if price > budget:
#         print(f"You don't have enough money!\nYou need {price - budget:.2f} leva!")
#         break
#     budget -= price
#     total += price
#
#
# days = int(input())
# hours = int(input())
# DayTotal = 0
# total = 0
# for i in range(days):
#     DayTotal = 0
#     for j in range(hours):
#         if (i+1) % 2 == 0 and (j+1) % 2 != 0:
#             price = 2.5
#         elif (i+1) % 2 != 0 and (j+1) % 2 == 0:
#             price = 1.25
#         else:
#             price = 1
#         DayTotal+=price
#     print(f"Day: {i+1} - {DayTotal:.2f} leva")
#     total +=DayTotal
# print(f"Total: {total:.2f} leva")