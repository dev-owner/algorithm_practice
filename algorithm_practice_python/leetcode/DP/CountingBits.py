from typing import List


class Solution:
    get_bin = lambda self, x: format(x, 'b')

    def countBits_1(self, n: int) -> List[int]:
        # for * count -> n^2
        arr = []
        for i in range(n + 1):
            print(self.get_bin(i))
            arr.append(self.get_bin(i).count('1'))

        return arr

    def countBits_2(self, n: int) -> List[int]:
        # 인덱스는 1씩 증가
        # 패턴이 있지 않을까?
        # 0 1 2 3 4 5 6 ..
        # 0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4 ..
        # 1 2 2 3 패턴이 보인다. -> sub problem으로 나눌 수 있다.
        # dp[0] = 0,
        # dp[1] = dp[0] + 1 = dp[1-1]
        # dp[2] = dp[0] + 1 = dp[2-2]
        # dp[3] = dp[1] + 1 = dp[3-2]
        # dp[4] = dp[0] + 1 = dp[4-4]
        # dp[5] = dp[1] + 1 = dp[5-4]
        # dp[6] = dp[2] + 1 = dp[6-4]
        # dp[7] = dp[3] + 1 = dp[7-4]
        # dp[index] = dp[index-offset] + 1
        # offset = 2^n
        arr = [0]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 <= i:
                offset *= 2
            arr.append(arr[i - offset] + 1)

        return arr

    def countBits(self, n: int) -> List[int]:
        # even = 2n, odd = 2n+1
        # x2 = adding 0 at the end
        # double = # of 1's
        # 2를 곱하면 뒤에 0 하나 붙인거랑 같음
        # 2 곱하고 1더하면 1 카운트가 하나 늘어남
        # countBits(N) = countBits(2N)
        # countBits(N) + 1 = CountBits(2N+1)
        # time, space = O(N)

        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter


if __name__ == '__main__':
    n = 5
    ans = Solution().countBits(n)
    print(f'{ans}, [0, 1, 1, 2, 1, 2]')
