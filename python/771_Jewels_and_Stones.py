import collections

class Solution:
    def numJewelsInStones_brute_force(self, J: str, S: str) -> int:
        result = 0
        for j in J:
            for s in S:
                if j == s:
                    result += 1

        return result

    def numJewelsInStones_hashtable(self, J: str, S: str) -> int:
        freqs = {}
        count = 0

        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in J:
            if char in freqs:
                count += freqs[char]
        
        return count

    def numJewelsInStones_defaultdict(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in S:
            freqs[char] += 1
        
        for char in J:
            count += freqs[char]
        
        return count


if __name__ == "__main__":
    ret = Solution().numJewelsInStones_defaultdict("aA", "aAAbbbb")
    print(ret)
