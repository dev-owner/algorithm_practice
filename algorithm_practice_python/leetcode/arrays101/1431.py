from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_amount = max(candies)
        for i in candies:
            if i + extraCandies >= max_amount:
                ans.append(True)
            else:
                ans.append(False)
        return ans

    def sol2(self, candies, extra):
        max_candies = max(candies)
        return [True if i+extra >= max_candies else False for i in candies]

if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    ans = Solution().sol2(candies, extraCandies)
    print(f'{ans}, [true,true,true,false,true]')
