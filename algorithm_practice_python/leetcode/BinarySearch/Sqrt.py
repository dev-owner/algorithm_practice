class Sqrt:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            mid = (left + right) // 2
            tgt = mid ** 2
            if tgt < x:
                left = mid + 1
            elif tgt > x:
                right = mid - 1
            else:
                return mid

        return right
