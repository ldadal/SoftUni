health = 100
bitcoins = 0
dungeons_room = input()
counter = 0

room = dungeons_room.split("|")
for i in range(len(room)):
    command, num = room[i].split()
    number = int(num)

    if command == "potion":
        if health + number > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
            print(f"Current health: {health} hp.")
        else:
            health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")

    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number

    else:
        if health - number > 0:
            print(f"You slayed {command}.")
            health -= number
        else:
            counter+=1
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter}")
            health -= number
            break

    counter += 1

if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
