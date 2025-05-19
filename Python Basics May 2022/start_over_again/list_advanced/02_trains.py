def comand(comands, railcars):
    while comands != "End":
        action = comands.split()
        if action[0] == "add":
            a = int(railcars[-1])
            railcars[-1] = a + int(action[1])
        elif action[0] == "insert":
            a = railcars.pop(int(action[1]))
            railcars.insert(int(action[1]),a + int(action[2]))
        else:
            a = railcars.pop(int(action[1]))
            railcars.insert(int(action[1]), a - int(action[2]))
        comands = input()
    return railcars


wagons = int(input())
train = [0] * wagons
comands = input()
print(comand(comands,train))
