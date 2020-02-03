# coding=utf-8

# Merge the Tools! (Medium)
# https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        s = list(string[i:i+k])
        ss = set(string[i:i+k])
        j = 0
        sr = ""
        while len(ss)>0 :
            if s[j] in ss:
                sr += s[j]
                ss.remove(s[j])

            j += 1

        print(sr)


if __name__ == '__main__':
#    string, k = input(), int(input())
    string, k = ("AABCAAADA", 3)
    merge_the_tools(string, k)

# pass