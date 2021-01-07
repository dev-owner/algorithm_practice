import pytest

from leetcode.google.fruit_into_baskets import FruitIntoBaskets


@pytest.mark.parametrize("tree, expected", [([0], 1), ([1, 2, 1], 3), ([0, 1, 2, 2], 3), ([1, 2, 3, 2, 2], 4),
                                            ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5)])
def test_fruit_into_baskets(tree, expected):
    obj = FruitIntoBaskets()

    assert obj.totalFruit(tree) == expected
