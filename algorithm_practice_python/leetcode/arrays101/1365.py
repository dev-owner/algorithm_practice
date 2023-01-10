from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # find the # of that nums[i] < others
        ans = []
        for i in nums:
            cnt = 0
            for j in nums:
                if i > j: cnt += 1
            ans.append(cnt)

        return ans

    def sol2(self, nums):
        temp = sorted(nums)
        mapping = {}
        result = []
        length = range(len(temp))
        for i in length:
            if temp[i] not in mapping:
                mapping[temp[i]] = i

        for i in length:
            result.append(mapping[nums[i]])

        return result

if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    ans = Solution().sol2(nums)
    print(f'{ans}, [4,0,1,1,3]')
