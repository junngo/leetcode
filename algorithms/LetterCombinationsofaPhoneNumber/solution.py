'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = {"2":"abc", "3":"def" , "4":"ghi", "5":"jkl",
                "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}        
        dial_list = []

        if len(digits) == 0:
            return dial_list

        for i in digits:
            dial_list.append(dial[i])

        ret = ["".join(s) for s in product(*dial_list)]

        return ret

if __name__ == '__main__':
    result = Solution().letterCombinations("")
    print(result)
