from functools import lru_cache


class Solution:
    def fib(self, n: int) -> int:
        """
            F(0) = 0, F(1) = 1
            F(n) = F(n-1) + F(n-2), for n > 1
        """
        if n == 0:
            return 0
        ans = [0] * (n + 1)
        ans[1] = 1
        for i in range(2, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2]

        return ans[-1]

    @lru_cache(maxsize=None)
    def fib1(self, n):
        if n < 2: return n
        return self.fib1(n - 1) + self.fib1(n - 2)

    def fib2(self, n):
        if n == 0: return 0
        dp = [0, 1]
        for _ in range(2, n + 1):
            dp = [dp[-1], dp[-1] + dp[-2]]
        return dp


    def fib3(self, n):
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a+b
        return a

if __name__ == '__main__':
    n = 4

    ans = Solution().fib3(n)
    print(f'{ans}, 3')
