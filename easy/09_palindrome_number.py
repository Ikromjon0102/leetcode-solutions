# 23.11.2023
# problem link 👉 https://leetcode.com/problems/palindrome-number/
# Ikromjon_Ergashev

# Runtime: 50ms => Beats 90.99%of users with Python3
# Memory: 16.34MB => Beats 11.50%of users with Python3

def isPalindrome(x: int) -> bool:
    return True if str(x) == str(x)[::-1] else False


