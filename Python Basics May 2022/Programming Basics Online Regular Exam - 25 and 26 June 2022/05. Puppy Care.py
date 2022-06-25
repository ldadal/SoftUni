food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
eat = input()
while eat != "Adopted":
    food_in_grams -= int(eat)
    eat = input()
if food_in_grams >= 0:
    print(f"Food is enough! Leftovers: {food_in_grams} grams.")
elif food_in_grams < 0:
    print(f"Food is not enough. You need {food_in_grams * -1} grams more.")
