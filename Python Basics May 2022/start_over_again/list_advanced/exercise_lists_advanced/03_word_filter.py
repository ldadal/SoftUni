text = input().split(" ")
result = [word for word in text if len(word)%2==0]
print(*[word for word in result], sep='\n')