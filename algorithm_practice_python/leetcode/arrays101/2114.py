from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split(" ")) for s in sentences])

    def sol2(self, ss):
        return max([s.count(" ") for s in ss]) + 1


if __name__ == '__main__':
    sentences = ["please wait","continue to fight","continue to win"]
    ans = Solution().sol2(sentences)
    print(f'{ans}, 3')
