# 23.01.2023
# problem link 👉 https://leetcode.com/problems/sqrtx/
# Ikromjon_Ergashev

# Runtime: 27 ms Beats 99.19% of users with Python3
# Memory: 16.57 MB Beats 56.48% of users with Python3

from math import sqrt, floor
class Solution:
    def mySqrt(self, x: int) -> int:
        return floor(sqrt(x))


print(Solution().mySqrt(12))