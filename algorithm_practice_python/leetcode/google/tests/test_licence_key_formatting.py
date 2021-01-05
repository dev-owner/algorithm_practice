import pytest

from leetcode.google.licence_key_formatting import LicenseKeyFormatting


@pytest.mark.parametrize("S,K,expected",
                         [("5F3Z-2e-9-w", 4, "5F3Z-2E9W"), ("2-5g-3-J", 2, "2-5G-3J"),
                          ("2-4A0r7-4k", 4, "24A0-R74K")])
def test_license_key_formatting(S, K, expected):
    obj = LicenseKeyFormatting()
    assert obj.licenseKeyFormatting(S, K) == expected
