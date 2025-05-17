def compare(first, second):
    for i in range(len(first)):
        if first[i] == second[i]:
            print(True)
        else:
            print(False)

numbs = input().split(", ")
reversed_numbs = []
for i in range(len(numbs)):
    reversed_numbs.append(numbs[i][::-1])
compare(numbs, reversed_numbs)