# coding=utf-8

# 난이도 : 상 (Hard)
# https://www.hackerrank.com/challenges/matrix-script/problem

# don't use `if` condition

#first_multiple_input = input().rstrip().split()
#
#n = int(first_multiple_input[0])
#
#m = int(first_multiple_input[1])
#
#matrix = []
#
#for _ in range(n):
#    matrix_item = input()
#    matrix.append(matrix_item)

import re

n = 7
m = 3
matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
#result : This is Matrix#  %!

s = ""
for i in range(m):
    for j in range(n):
        s += matrix[j][i]

print(re.sub(r"([A-Za-z0-9])([!@#$%& ]+)([A-Za-z0-9])", r"\1 \3", s))

# pass


