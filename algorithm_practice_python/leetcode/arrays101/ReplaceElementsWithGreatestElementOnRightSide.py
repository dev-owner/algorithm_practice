class Solution(object):
    # OK, but too complecated.
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     max = -1
    #     temp = 0
    #     for idx, val in reversed(list(enumerate(arr))):
    #         if max < val:
    #             temp = val
    #             arr[idx] = max
    #             max = temp
    #         else:
    #             arr[idx] = max
    #     return arr

    # OK, go to pythonic code
    def replaceElements(self, arr):
        saved, arr[-1] = arr[-1], -1

        for i in range(len(arr) - 2, -1, -1):
            arr[i], saved = saved, max(saved, arr[i])

        return arr
