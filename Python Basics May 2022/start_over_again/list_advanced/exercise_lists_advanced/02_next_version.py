current_version = [int(v) for v in input().split(".")]
if current_version[2] + 1 > 9:
    current_version[2] = 0
    if current_version[1] + 1 > 9:
        current_version[0] += 1
        current_version[1] = 0
    else:
        current_version[1] += 1
else:
    current_version[2] += 1
# result = [0 if num+1 > 9 else num+1 for num in current_version]
print(*current_version, sep=".")
# print(*result, sep=".")
