'''
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

    def reverse_two_pointer(self, s: List[str]) -> None:
        start, end = 0 , len(s)-1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    in_val = ["h","e","l","l","o"]
    # ret = Solution().reverse_two_pointer(in_val)
    ret = Solution().reverse_two_pointer(in_val)

    print(in_val)
