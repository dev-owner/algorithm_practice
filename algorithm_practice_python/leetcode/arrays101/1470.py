from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # input : x1 x2 xn, y1 y2 yn
        # return x1 y1 x2 y2 xn yn

        ans = []
        size = len(nums) // 2
        for i in range(0, size):
            ans.append(nums[i])
            ans.append(nums[size + i])

        return ans

    def sol2(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res





if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    ans = Solution().shuffle(nums, n)
    print(f'{ans}, [2,3,5,4,1,7] ')
