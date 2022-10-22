shoppin_list = input().split("!")
info_data = input()


while info_data != "Go Shopping!":

    if "Correct" in info_data:
        _, old_item, new_item = info_data.split()
        if old_item in shoppin_list:
            shoppin_list[shoppin_list.index(old_item)] = new_item
        info_data = input()
        continue

    command, item = info_data.split()

    if command == "Urgent":
        if item not in shoppin_list:
            shoppin_list.insert(0, item)

    elif command == "Unnecessary":
        if item in shoppin_list:
            shoppin_list.remove(item)

    elif command == "Rearrange":
        if item in shoppin_list:
            shoppin_list.remove(item)
            shoppin_list.append(item)

    info_data = input()

print(*shoppin_list, sep=", ")