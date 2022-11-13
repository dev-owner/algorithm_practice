class Solution:
    def divisorGame(self, n: int) -> bool:
        """
            alice가 게임 먼저 시작
            약수로 현재 숫자 빼면서 더이상 뺄 수 없으면 지는게임
            optimal하게 움직인다고 가정 -> 특정 숫자에서 결과는 정해짐
            dp[i] = True if the player starting with number i wins, else False
            1 <= i <= 1000
            n = 2 -> true
            n = 3 -> false
            n = 4 -> true
        """

        dp = [False for _ in range(n+1)]
        for i in range(n+1):
            for j in range(1, i//2+1):
                if i % j == 0 and (not dp[i-j]):
                    dp[i] = True
        return dp[n]



if __name__ == '__main__':
    n = 4
    ans = Solution().divisorGame(n)
    print(f'{ans}, true')
