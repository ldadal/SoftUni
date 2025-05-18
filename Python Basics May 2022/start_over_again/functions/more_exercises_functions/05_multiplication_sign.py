def sing(n1, n2, n3):
    result = ""
    if n1 == 0 or n2 == 0 or n3 == 0:
        result = "zero"
    elif n1 > 0 and n2 > 0 and n3 > 0:
        result = "positive"
    elif n1 < 0 and n2 < 0 and n3 > 0:
        result = "positive"
    elif n1 < 0 and n2 > 0 and n3 < 0:
        result = "positive"
    elif n1>0 and n2<0 and n3<0:
        result = "positive"
    else:
        result = "negative"
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(sing(first_num,second_num,third_num))