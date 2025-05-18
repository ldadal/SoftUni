def manipulate_data(type, data_to_manipulate):
    if type == "int":
        data_to_manipulate = int(data_to_manipulate)
        return data_to_manipulate * 2
    elif type == "real":
        data_to_manipulate = float(data_to_manipulate)
        return f"{data_to_manipulate * 1.5:.2f}"
    else:
        return f"${data_to_manipulate}$"


type_data = input()
data = input()
print(manipulate_data(type_data, data))