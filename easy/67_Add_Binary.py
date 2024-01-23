# 23.01.2023
# problem link 👉 https://leetcode.com/problems/add-binary/description/
# Ikromjon_Ergashev

# Runtime: 39 ms Beats 62.63% of users with Python3
# Memory: 16.42 MB Beats 65.75% of users with Python3

def addBinary(a: str, b: str) -> str:
    c = int(a, base = 2) + int(b, base = 2)
    return bin(c)[2:]


print(addBinary("11","1"))