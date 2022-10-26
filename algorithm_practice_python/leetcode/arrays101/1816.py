class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


if __name__ == '__main__':
    s = "Hello how are you Contestant"
    k = 4
    r = Solution().truncateSentence(s, k)
    print(f"{r}, Hello how are you")
