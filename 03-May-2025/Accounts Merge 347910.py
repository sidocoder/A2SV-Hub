# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        roots = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            roots[root].append(email)

        merged_accounts = []
        for root, emails in roots.items():
            merged_accounts.append([email_to_name[root]] + sorted(emails))

        return merged_accounts
