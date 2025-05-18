import cmath
import math
from math import floor


def longest_line(first_line, second_line):
    line_one_dist_start_point = first_line[0]*first_line[0] + first_line[1]*first_line[1]
    line_one_dist_end_point = first_line[2]*first_line[2] + first_line[3]*first_line[3]
    line_two_dist_start_point = second_line[0]*second_line[0] + second_line[1]*second_line[1]
    line_two_dist_end_point = second_line[2]*second_line[2] + second_line[3]*second_line[3]
    line_one_len = line_one_dist_start_point*line_one_dist_start_point + line_one_dist_end_point*line_one_dist_end_point
    line_two_len = line_two_dist_start_point*line_two_dist_start_point + line_two_dist_end_point*line_two_dist_end_point
    if line_two_len > line_one_len:
        if line_two_dist_start_point > line_two_dist_end_point:
            return f"({floor(second_line[2])}, {floor(second_line[3])})({floor(second_line[0])}, {floor(second_line[1])})"

        else:

            return f"({floor(second_line[0])}, {floor(second_line[1])})({floor(second_line[2])}, {floor(second_line[3])})"
    else:
        if line_one_dist_start_point > line_one_dist_end_point:

            return f"({floor(first_line[2])}, {floor(first_line[3])})({floor(first_line[0])}, {floor(first_line[1])})"
        else:

            return f"({floor(first_line[0])}, {floor(first_line[1])})({floor(first_line[2])}, {floor(first_line[3])})"


first_line = []
second_line = []
for _ in range(4):
    first_line.append(float(input()))
for _ in range(4):
    second_line.append(float(input()))
print(longest_line(first_line,second_line))



