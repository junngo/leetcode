'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
'''

class Solusion:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False

            else:
                stack.append(char)

        return not stack

    def isValid2(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        
        return len(stack) == 0


if __name__=='__main__':
	str = Solusion().isValid("()[]{}")
	print(str)
