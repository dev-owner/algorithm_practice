import pytest

from leetcode.google.UniqueEmailAddresses import UniqueEmailAddresses


@pytest.fixture
def emails():
    rv = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]
    return rv


@pytest.fixture
def unique():
    return UniqueEmailAddresses()


class TestUniqueEmailAddresses:
    def test_num_unique_emails(self, emails, unique):
        assert unique.numUniqueEmails(emails) == 2
