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

class Solusion(object):
    def myAtoi1(self, str):

        retInt = 0
        tempStr = str.strip()
        minusFlag = False

        try:
            if tempStr[0] is '-':
                minusFlag = True
                tempStr = tempStr[1:]
        except:
            return 0

        for i in range(0, len(tempStr)):
            if i == 0 and ((tempStr[i] < '0') or (tempStr[i] > '9')):
                return 0
            elif(tempStr[i] >= '0') and (tempStr[i] <= '9'):
                retInt = (retInt*10) + int(tempStr[i])
            else:
                break

        if minusFlag is True:
            retInt *= -1

        return retInt

    def myAtoi2(self, str):
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = 0

        if not str:
            return result

        i = 0
        while i < len(str) and str[i].isspace():
            i += 1

        if len(str) == i:
            return result

        sign = 1
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1

        while i < len(str) and '0' <= str[i] <= '9':
            if result > (INT_MAX - int(str[i])) / 10:
                return INT_MAX if sign > 0 else INT_MIN
            result = result * 10 + int(str[i])
            i += 1

        return sign * result


if __name__=='__main__':
	integers = Solusion().myAtoi2('    -42')
	print(integers)
