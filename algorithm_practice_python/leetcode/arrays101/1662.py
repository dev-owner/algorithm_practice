from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    ans = Solution().arrayStringsAreEqual(word1, word2)
    print(f'{ans}, true')
