class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        for (i in nums.indices) {
            val findValue = target - nums[i]
            for (j in i+1 until nums.size) {
                if (nums[j] == findValue) {
                    return intArrayOf(i, j)
                }
            }
        }
        return intArrayOf()
    }
}

fun main() {
    val solution = Solution()
    val nums = intArrayOf(2, 7, 11, 15)
    val target = 9

    val result = solution.twoSum(nums, target)
    println("Indices: ${result[0]} ${result[1]}")
}
