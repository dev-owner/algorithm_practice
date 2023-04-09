import itertools
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3개 숫자 더해서 0이 나오는 숫자들의 리스트 반환
        # distinct
        # i, j, k는 모두 달라야함
        # <= 3000 이므로 n^2까지는 가능
        # nums[i] <= 10,
        # 접근은..
        # 중복도 의미가 있음. 동시에 사용 가능
        # n개중 3개 뽑는 경우의 수
        # 순서 상관 없으니 조합으로 가면 될듯
        # O(N^2logN) => time exceeded


        nCr = set(itertools.combinations(nums, 3))
        ret = []
        for c in nCr:
            if sum(c) == 0:
                sorted_val = sorted(list(c))
                if sorted_val not in ret:
                    ret.append(sorted_val)
        return ret

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        # combination은 O(n!)이므로 <=3000 입력에는 사용안된다.
        # n! 으로 재구현 필요

        ret = []
        return ret

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    ans = Solution().threeSum2(nums)
    print(f'{ans}, [[-1,-1,2],[-1,0,1]]')
