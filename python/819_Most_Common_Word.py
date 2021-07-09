import collections
import re

class Solution:
    def mostCommonWord_dict(self, paragraph: str, banned: List[str]) -> str:
        s = re.sub(r"[^\w]", " ", paragraph.lower())
        words = s.split()
        count = collections.defaultdict(int)
        for word in words:
            if word in banned:
                continue

            count[word] += 1

        return max(count, key=count.get)


    def mostCommonWord_counter(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                    .lower().split()
                        if word not in banned]
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]
