text = input()
result = [char for char in text if char.lower() not in ['a', 'o', 'i', 'u', 'e']]
print("".join(result))