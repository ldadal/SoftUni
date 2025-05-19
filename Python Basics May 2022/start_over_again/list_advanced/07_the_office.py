employees_happiness = [int(empl) for empl in input().split()]
multiply = int(input())
after_multiply = [hap * multiply for hap in employees_happiness]
avarage_hap = sum(after_multiply) / len(employees_happiness)
happy_empl = list(filter(lambda x: x >= avarage_hap, after_multiply))
if len(happy_empl) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_empl)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_empl)}/{len(employees_happiness)}. Employees are not happy!")