# 24.11.2023
# problem link 👉 https://leetcode.com/problems/create-target-array-in-the-given-order
# Ikromjon_Ergashev

# Runtime: 47ms => Beats 17.22%of users with Python3
# Memory:  16.31MB => Beats 10.59%of users with Python3

def createTargetArray(nums, index):
    a = []
    for k, i in zip(nums, index):
        a.insert(i, k)
    return a

# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
# output = [0,4,1,3,2]
# print(romanToInt(nums, index))