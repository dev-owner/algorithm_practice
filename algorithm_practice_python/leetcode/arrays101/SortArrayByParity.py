from typing import List


class SortArrayByParity:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        slow = 0
        for fast in range(len(A)):
            if A[fast] % 2 == 0:
                A[slow], A[fast] = A[fast], A[slow]
                slow += 1
        return A
