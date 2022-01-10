class Solution:
    def solve(self, A, B, C):
        if A>B:
            A = A%B
        if C>B:
            C = C%B
        ans = C+A-1
        if ans>B:
            ans = ans%B

        return ans
