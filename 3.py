class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        s = 0
        p = 1
        res = 0
        for e in range(len(arr)):
            p *= arr[e]
            while p>= k and s<e:
                p = p//arr[s]
                s+=1
            if p<k:
                le = e-s+1
                res += le
                
        return res
    
