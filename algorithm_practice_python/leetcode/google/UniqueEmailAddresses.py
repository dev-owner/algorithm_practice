class UniqueEmailAddresses:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        rv = []
        for email in emails:
            e = email.split('@')
            e[0] = e[0].split('+', 1)[0].replace('.', '')
            rv.append('@'.join(e))

        rv = set(rv)

        return len(rv)
