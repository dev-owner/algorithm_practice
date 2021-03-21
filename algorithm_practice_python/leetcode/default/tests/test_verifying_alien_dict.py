import pytest

from leetcode.default.verifying_alien_dict import Solution


@pytest.mark.parametrize("words, order, expected",
                         [(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
                          (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
                          (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False)]
                         )
def test_is_alien_sorted(words, order, expected):
    assert Solution().isAlienSorted(words, order) == expected
