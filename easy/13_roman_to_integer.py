# 23.11.2023
# problem link 👉 https://leetcode.com/problems/roman-to-integer/
# Ikromjon_Ergashev

# Runtime: 55ms => Beats 38.38%of users with Python3
# Memory: 16.27MB => Beats 54.30%of users with Python3

def romanToInt(s: str) -> int:
    rim_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    a = list(map(lambda x: rim_numbers.get(x), s))
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] < a[i + 1]:
            summ -= a[i]
        else:
            summ += a[i]
    return summ

