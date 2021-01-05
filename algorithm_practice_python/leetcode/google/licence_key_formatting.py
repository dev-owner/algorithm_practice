class LicenseKeyFormatting:
    """
        S, K가 있을때, 대시 사이 알파벳이 정확히 K길이만큼 되도록 조정
        만약 첫번째 그룹이 K보다 작으면, 해당 그룹은 제외
    """

    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        print(S)
        return "-".join([S[i:i+K] for i in range(0, len(S), K)])[::-1]
