# 23.11.2023
# problem link 👉 https://leetcode.com/problems/add-two-numbers/
# Ikromjon_Ergashev

# Runtime:
# Memory:

# def addTwoNumbers(l1,l2):
#     a = ''.join(list(map(str,l1)))
#     b = ''.join(list(map(str,l2)))
#     l3 = str(int(a) + int(b))
#     l3 = list(l3)
#     return list(map(int,l3[::-1]))
#
# l1 = [2,4,3]
# l2 = [5,6,4]
# print(addTwoNumbers(l1, l2))
# # [7,0,8]
# def findMedianSortedArrays(nums1,nums2) -> float:
    # a = nums1 + nums2
    # a.sort()
    # if len(a) % 2 == 0:
    #     b = len(a) // 2
    #     summ = a[b] + a[b - 1]
    #     return '{:.5f}'.format(summ)
    # else:
    #     b = len(a) // 2
    #     summ = a[b]
    #     return '{:.5f}'.format(summ)

# print(findMedianSortedArrays([1,3],[2]))



a = list(map(int, '123456'))
print(a)