
class Solution:
    def canPair(self, arr, k):
        d = {}
        for i in range(len(arr)):
            rem = arr[i]%k
            try:
                if d[rem]:
                    d[rem] += 1
            except:
                d[rem] = 1
                
        for i,v in d.items():
            temp1 = d[i]%2
            #case 1 k//2
            if i == k//2 and k%2 == 0 :
                if temp1 != 0:
                    return False

            #Case rem == 0
            elif i == 0:
                if temp1 != 0:
                    return False
            
            #CAse Normal
            else:
                temp = k-i
                total = d[i]
                try:
                    if d[temp] and d[temp] == total:
                        pass
                    else:
                        return False
                except:
                    return False
                    
        return True
