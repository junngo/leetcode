'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "-42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.

'''

class Solusion:
    def myAtoi(self, str: str) -> int:
        pos_limit = 0x7fffffff
        neg_limit = -0x80000000

        temp_str = str.strip()
        minus_flag = False
        ret_num = ''

        if temp_str.startswith('-'):
           temp_str = temp_str[1:]

           minus_flag = True

        elif temp_str.startswith('+'):
           temp_str = temp_str[1:]

        if (temp_str == "") or (not temp_str[0].isdigit()):
            return 0

        for s in temp_str:
            if not s.isdigit():
                break
            ret_num += s

        ret_num = int(ret_num)
        if ret_num == 0:
            return ret_num

        elif minus_flag:
            ret_num *= -1
            if (ret_num & neg_limit) != neg_limit:
                return neg_limit

        elif (ret_num & pos_limit) != ret_num:
            return pos_limit

        return ret_num


if __name__=='__main__':
	integers = Solusion().myAtoi('     ')
	print(integers)
