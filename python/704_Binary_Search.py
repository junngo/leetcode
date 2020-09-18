class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid

            else:
                return -1

        return binary_search(0, len(nums) - 1)


if __name__ == "__main__":
    ret = Solution().search([-1, 0, 3, 5, 9, 12], 9)
    print(ret)
