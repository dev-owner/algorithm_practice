from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        base = 0
        for op in operations:
            if op[0] == '-' or op[-1] == '-':
                base -= 1
            elif op[0] == '+' or op[-1] == '+':
                base += 1
        return base

    def sol2(self, operations):
        op_dict = {"-": -1, "+": 1}
        return sum(op_dict[op[1]]for op in operations)

if __name__ == '__main__':
    operations = ["--X","X++","X++"]
    ans = Solution().sol2(operations)
    print(f'{ans}, 1')
