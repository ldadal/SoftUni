words = [word for word in input().split(" ")]
palindrome_words = [word for word in words if word[::-1] == word]
palindrome_to_campare = input()
print(palindrome_words)
count = 0
for i in range(len(palindrome_words)):
    if palindrome_to_campare == palindrome_words[i]:
        count += 1
print(f"Found palindrome {count} times")
