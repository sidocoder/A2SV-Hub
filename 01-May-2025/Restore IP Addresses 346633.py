# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(part: str) -> bool:
            return len(part) > 0 and (part == "0" or (part[0] != "0" and int(part) <= 255))

        res = []
        n = len(s)

        for i in range(1, min(4, n - 2)):
            for j in range(i + 1, min(i + 4, n - 1)):
                for k in range(j + 1, min(j + 4, n)):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if all(map(is_valid, [a, b, c, d])):
                        res.append(f"{a}.{b}.{c}.{d}")
        return res
