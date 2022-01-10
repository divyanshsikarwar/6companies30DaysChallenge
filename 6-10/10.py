class Solution:

    def matchPairs(self,nuts, bolts, n):
        nuts.sort()
        bolts.sort()
        ans = []
        for i in range(n):
            if nuts[i]== bolts[i]:
                ans.append(nuts[i])
                
        return 