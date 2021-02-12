import pytest

from leetcode.Graph.find_the_town_judge import Solution


@pytest.mark.parametrize("N, trust, expected", [(2, [[1, 2]], 2), (3, [[1, 3], [2, 3]], 3),
                                                (3, [[1, 3], [2, 3], [3, 1]], -1),
                                                (4, [[1, 2], [2, 3]], -1),
                                                (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
                                                (4, [[1, 3], [1, 4], [2, 3]], -1)])
def test_find_judge(N, trust, expected):
    s = Solution()
    """
    4
    
    """
    assert s.findJudge(N, trust) == expected
