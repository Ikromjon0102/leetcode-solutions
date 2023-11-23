# 23.11.2023
# problem link 👉 https://leetcode.com/problems/two-sum/
# Ikromjon_Ergashev

# Runtime: 1954ms => Beats 35.15%of users with Python3
# Memory: 17.21MB => Beats 58.84%of users with Python3

def twoSum(nums,  target):
    for i in nums:
        for j in nums[nums.index(i)+1:]:
            if i + j == target:
                print(i, j)
                if i == j:
                    b = nums.index(i)
                    nums.remove(i)
                    c = nums.index(j) + 1
                    return [b, c]
                else:
                    a = [nums.index(i), nums.index(j)]
                    return a
