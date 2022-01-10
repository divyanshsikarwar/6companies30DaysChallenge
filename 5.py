class Solution:
    def getNthUglyNo(self,n):
        li = [1]
        twoP = 0
        threeP = 0
        fiveP = 0
        # code here
        while len(li)<n:
            two_V = li[twoP]*2
            three_V = li[threeP]*3
            five_V = li[fiveP]*5
            mi = min(three_V,two_V,five_V)
            
            if mi == three_V:
                threeP+=1
            if mi == five_V:
                fiveP+=1
            if mi == two_V:
                twoP+=1
                
            li.append(mi)
            
        return li[-1]
