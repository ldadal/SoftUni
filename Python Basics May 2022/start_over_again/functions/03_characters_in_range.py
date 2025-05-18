def all_chars(start_char, end_char):
    result = ""
    for ascii_value in range(ord(start_char) + 1, ord(end_char)):
        result += f"{chr(ascii_value)} "
    return result


char_one = input()
char_two = input()
print(all_chars(char_one, char_two))
