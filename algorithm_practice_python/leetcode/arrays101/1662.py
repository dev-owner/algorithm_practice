from typing import List


class Solution:
    # time: O(N)
    # space: O(N)
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    def sol2(self, w1, w2):
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True

    def generate(self, w):
        # time : O(N+M)
        # space: O(1)
        for word in w:
            for char in word:
                yield char
        yield None

if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    ans = Solution().sol2(word1, word2)
    print(f'{ans}, true')
