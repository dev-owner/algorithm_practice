from typing import List


class SumOfSubarrayMinimums:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        모든 연속된 부분집합을 찾고 각 부분집합에서 가장 작은 값의 합을 구해라
        일단 자기자신, 그리고 오른쪽으로 최대길이까지 순차적으로 증가
        11,81,94,43,3

        #11              11      0

        11,81           11      1
        #81              81      1

        11,81,94        11      2
        81,94           81      2
        #94              94      2

        11,81,94,43     11      3
        81,94,43        43      3
        94,43           43      3
        #43              43      3

        11,81,94,43,3   3       4
        81,94,43,3      3       4
        94,43,3         3       4
        43,3            3       4
        #3               3       4

        cache = list
        for i, v in enumerate(arr)
            cache.append(v)



        """

        ret = 0
        mod = 1e9
        prev = []
        for idx, v in enumerate(arr):


        return int(ret % mod)
