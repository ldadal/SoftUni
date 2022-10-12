first = list(input())
second = list(input())
counter=0
for i in first:
    if first[counter]==second[counter]:
        counter+=1
        continue
    else:
        first[counter]=second[counter]
        counter+=1
        print("".join(first))
