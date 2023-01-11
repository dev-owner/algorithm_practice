from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for idx, i in enumerate(encoded):
            arr.append(i ^ arr[idx])
        return arr

    def sol2(self, encoded, first):
        arr = [first]
        for i in encoded:
            arr.append(arr[-1] ^ i)
        return arr


if __name__ == '__main__':
    encoded = [1, 2, 3]
    first = 1

    ans = Solution().sol2(encoded, first)
    print(f'{ans}, [1,0,2,1]')
