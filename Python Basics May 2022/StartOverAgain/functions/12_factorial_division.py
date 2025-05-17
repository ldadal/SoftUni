def calculate(num_one, num_two):
    fact_num_one = 1
    fact_num_two = 1
    for n in range(1,num_one+1):
        fact_num_one *= n
    for n in range(1,num_two+1):
        fact_num_two *= n
    sum = fact_num_one/fact_num_two
    return sum


num1 = int(input())
num2 = int(input())
print(f"{calculate(num1,num2):.2f}")