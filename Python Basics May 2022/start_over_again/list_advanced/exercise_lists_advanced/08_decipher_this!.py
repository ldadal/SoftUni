codes = input().split()
word = ""
nums = ""
for x in range(len(codes)):
    for index in range(0,len(codes[x])):
        if codes[x][index].isalpha():
            word+=codes[x][index]
        elif codes[x][index].isnumeric():
            nums+=codes[x][index]
    # nums = list(reversed(nums))
    if len(word)>1:
        word = word[-1] + word[1:-1] + word[0]
    num=int(''.join(nums))
    print(chr(num) + word,end=" ")
    # print(chr(num),end="")
    # print(word,sep=" ")
    word = ""
    nums = ""