from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
            items[i] = [type, color, name]
        """
        mapping_table = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        cnt = 0
        for item in items:
            if item[mapping_table[ruleKey]] == ruleValue: cnt += 1

        return cnt


    def sol2(self, items, key, value):
        t = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 for item in items if item[t[ruleKey]] == ruleValue)

if __name__ == '__main__':
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
             ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    ans = Solution().sol2(items, ruleKey, ruleValue)
    print(f'{ans}, 1')
