def all_chars (start_char, end_char):
    for ascii_value in range(ord(start_char) + 1, ord(end_char)):
        print(chr(ascii_value), end=" ")


char_one = input()
char_two = input()
all_chars(char_one,char_two)