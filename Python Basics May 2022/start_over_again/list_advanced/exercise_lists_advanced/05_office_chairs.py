numbers_of_rooms = int(input())
chairs = []
people = []
while numbers_of_rooms != 0:
    numbers_of_rooms -= 1
    room = [x for x in input().split(" ")]
    chairs.append(room[0])
    people.append(int(room[1]))
chairs_count = []
for i in range(len(chairs)):
    chairs_count.append(len(chairs[i]))

print(
    *[f"{people[index] - chairs_count[index]} more chairs needed in room {index + 1}" for index in range(len(people)) if
      people[index] > chairs_count[index]], sep="\n")
a = 0
for i in range(len(chairs_count)):
    if chairs_count[i] < people[i]:
        a += 1
        break
if a == 0:
    print(f"Game On, {sum(chairs_count) - sum(people)} free chairs left")
