from typing import List


class OddEvenJump:
    def oddEvenJumps(self, A: List[int]) -> int:
        """
        odd jump, even jump가 있고 index i부터 j까지 (i<j) 이동해야 함
        odd jump는 index j 까지 A[i] <= A[j] 이면서 A[j]가 가장 작은 값으로 점프 가능. j 대상이 여러개면 가장 작은 j.
        even jump는 index j 까지 A[i] >= A[j] 이면서 A[j]가 가장 큰 값으로 점프 가능. j 대상이 여러개면 가장 작은 j.
        특정 i는 점프를 못할 수도 있음.

        좋은 출발 index는 해당 index에서 출발 했을 때, 배열의 끝에 도달할 수 있어야 함. (0번 이상 점프하여)
        좋은 스타팅 인덱스의 갯수를 반환해라.
        """

        # [10, 13, 12, 14, 15]

        length = len(A)
        odd = [False for _ in A]
        even = [False for _ in A]
        odd[length - 1] = True
        even[length - 1] = True

        for i in range(length - 2, -1, -1):
            if OddEvenJump.get_smallest_among_bigger(A, i):
                odd[i] = even[OddEvenJump.get_smallest_among_bigger(A, i)]
            else:
                odd[i] = False
            if OddEvenJump.get_biggest_among_smaller(A, i):
                even[i] = odd[OddEvenJump.get_biggest_among_smaller(A, i)]
            else:
                even[i] = False

        return len(list(filter(lambda x: x is True, odd)))

    @classmethod
    def get_smallest_among_bigger(cls, A, i):
        sub_arr = A[i + 1:]
        val = A[i]
        sub_arr.sort()
        for v in sub_arr:
            if val <= v:
                ret = A.index(v)
                if ret > i:
                    return ret
        return None

    @classmethod
    def get_biggest_among_smaller(cls, A, i):
        sub_arr = A[i + 1:]
        val = A[i]
        for v in reversed(sub_arr):
            if val >= v:
                ret = A.index(v)
                if ret > i:
                    return ret
        return None
