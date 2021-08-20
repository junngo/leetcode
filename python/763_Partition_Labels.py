class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []

        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans


if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    result = Solution().partitionLabels(s)
    print(result)
