import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 같은 숫자 반복 수가 중복된게 없으면 true, 있으면 false
        # time: O(n)
        # space: O(2n)
        ans = collections.defaultdict(int)
        for num in arr:
            ans[num] += 1

        s = set(ans.values())

        if len(s) == len(ans.values()):
            return True

        return False

    def uniqueOccurrences2(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))


if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    ans = Solution().uniqueOccurrences2(arr)
    print(f'{ans}, true')
