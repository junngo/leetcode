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

class Solusion(object):
	def findMedianSortedArrays(self, num1, num2):
		tempList = num1 + num2
		tempList.sort()

		if len(tempList)%2 == 0:
			return (tempList[(len(tempList)/2)-1] + tempList[len(tempList)/2]) / 2.0

		else:
			return tempList[len(tempList)/2]

if __name__=='__main__':
	num = Solusion().findMedianSortedArrays([1,3], [2])
	print(num)
