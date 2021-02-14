import pytest

from leetcode.Graph.symmetric_tree import Solution
from leetcode.Graph.symmetric_tree import TreeNode


def create_bTree(data, idx):
    if len(data) - 1 < idx:
        return
    if not data[idx]:
        return
    pnode = TreeNode(data[idx])
    pnode.left = create_bTree(data, 2 * idx + 1)
    pnode.right = create_bTree(data, 2 * idx + 2)
    return pnode


@pytest.mark.parametrize("input, expected", [(create_bTree([1, 2, 2, 3, 4, 4, 3], 0), True),
                                             (create_bTree([1, 2, 2, None, 3, None, 3], 0), False)])
def test_is_symmetric(input, expected):
    s = Solution()
    assert s.isSymmetric(input) is expected
