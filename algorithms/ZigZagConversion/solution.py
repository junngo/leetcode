'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solusion:
    def convert(self, s: str, numRows: int) -> str:
        arrayIdx = min(numRows, len(s))
        tmpString = [[] for i in range(arrayIdx)]
        retString = ""
        curRow = 0
        upGoing = False

        if (len(s) < numRows) or (numRows == 1):
            return s

        for c in s:
            tmpString[curRow].append(c)

            if (curRow == 0) or (curRow == (numRows - 1)):
                upGoing = not upGoing

            if upGoing:
                curRow += 1
            else:
                curRow -= 1

        for i in range(arrayIdx):
            retString += "".join(tmpString[i])

        return retString


if __name__=='__main__':
	str = Solusion().convert("PAYPALISHIRING", 3)
	print(str)
