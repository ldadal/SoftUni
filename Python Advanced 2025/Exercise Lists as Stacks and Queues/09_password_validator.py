# def pass_checker(password):
#     count = 0
#     symbol_checker = 0
#     for sym in password:
#         s = ord(sym)
#         if sym.isdigit():
#             count += 1
#         if sym.isalnum():
#             symbol_checker += 1
#     if 6 > len(password) or len(password) > 10:
#         print("Password must be between 6 and 10 characters")
#     if symbol_checker < len(password):
#         print("Password must consist only of letters and digits")
#     if count < 2:
#         print("Password must have at least 2 digits")
#     if len(password) >= 6 and len(password) <= 10 and symbol_checker == len(password) and count >= 2:
#         print("Password is valid")


def lenght_cheker(password):
    if 6 <= len(password) <= 10:
        return True


def sym_checker(password):
    sym_count = 0
    for sym in password:
        if sym.isalnum():
            sym_count += 1
    return sym_count


def digit_checker(password):
    count_digit = 0
    for n in password:
        if n.isdigit():
            count_digit += 1
    return count_digit


password = input()
if not lenght_cheker(password):
    print("Password must be between 6 and 10 characters")
if sym_checker(password) < len(password):
    print("Password must consist only of letters and digits")
if digit_checker(password) < 2:
    print("Password must have at least 2 digits")
if lenght_cheker(password) and sym_checker(password) == len(password) and digit_checker(password) >= 2:
    print("Password is valid")
