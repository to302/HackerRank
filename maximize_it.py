# coding=utf-8

# Maximize It! (Hard)
# https://www.hackerrank.com/challenges/maximize-it/problem



k, m = map(int, input().split())

s = 0
ll = []
for _ in range(k):
    l = list(map(lambda x: pow(x,2), map(int, input().split())))
    ll.append(l)






"""
7 588
7 3729019 6589533 9497010 1956867 4094190 1785314 9410145
7 6241592 9563118 4665482 3629252 418388 795859 816643
7 7924805 2362312 7324277 3672134 1005196 8234278 9131319
7 9978282 1999589 9658103 7451768 20958 1718778 3850870
7 4802255 5530524 3732809 8531273 2120056 3229818 488140
7 8730597 7531483 2414636 7488541 7094601 7080117 3634144
7 7512988 392327 4450786 7954145 2754638 4291414 1626278

587
"""