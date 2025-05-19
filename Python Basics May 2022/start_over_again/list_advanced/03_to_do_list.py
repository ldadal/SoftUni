def to_do_list(command):
    to_do = []
    list_of_comands = []
    while command != "End":
        list_of_comands.append(command)
        command = input()
    list_of_comands.sort()
    last_element = 0
    for i in range(len(list_of_comands)-1):
        a = list_of_comands[i]
        if a.startswith("10"):
            last_element = list_of_comands.pop(i).split("-")[1]
    for _ in range(len(list_of_comands)):
        to_do.insert(0, list_of_comands.pop().split("-")[1])
    if last_element != 0:
        to_do.append(last_element)
    return to_do


command = input()