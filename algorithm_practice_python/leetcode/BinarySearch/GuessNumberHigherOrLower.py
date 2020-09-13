class GuessNumberHigherOrLower:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            t = guess(m)
            if t == 0:
                return m
            elif t < 0:
                r = m - 1
            else:
                l = m + 1

        return -1
