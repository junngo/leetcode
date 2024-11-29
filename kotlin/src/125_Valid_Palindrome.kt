import java.util.*

/*
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
*/
fun isPalindrome(s: String): Boolean {
    val cleansingStr = s.lowercase(Locale.getDefault()).filter { it.isLetter() }
    val length = cleansingStr.length
    for(i in 0 until length / 2) {
        val frontChar = cleansingStr[i]
        val backChar = cleansingStr[length - i - 1]
        if (frontChar != backChar)
            return false
    }
    return true
}

fun main() {
    val str = "A man, a plan, a canal: Panama"
    val result = isPalindrome(str)
    print(result)
}
