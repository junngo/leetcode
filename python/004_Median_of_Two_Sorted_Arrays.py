'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

from typing import List
import statistics

class Solusion(object):
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(nums1+nums2)

	def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
		join_list = nums1 + nums2
		join_list.sort()

		quotient, remainder = divmod(len(join_list), 2)

		if remainder == 1:
			return join_list[quotient]

		return sum(join_list[quotient-1:quotient+1]) / 2

if __name__=='__main__':
	num = Solusion().findMedianSortedArrays2([1, 2, 3], [4, 5, 6])
	print(num)
