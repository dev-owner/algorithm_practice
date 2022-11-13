
def get_max_divisor(n):
    ans = 1
    for i in range(1, n):
        if n % i == 0:
            ans = i
    return ans

class Solution:
    def divisorGame(self, n: int) -> bool:
        i = 1
        while True:
            if n <= 1 : break
            x = get_max_divisor(n)
            n = n - x
            i = i + 1
        return True if i % 2 == 0 else False


if __name__ == '__main__':
    n = 4
    ans = Solution().divisorGame(n)
    print(f'{ans}, true')
