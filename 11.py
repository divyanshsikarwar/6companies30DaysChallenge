class Solution:
    def findTwoElement( self,arr, n): 
        miss = [0]*(len(arr))
        twice = 0
        for i in range(len(arr)):
            if miss[arr[i]-1] == 0:
                miss[arr[i]-1] = 1
            elif miss[arr[i]-1] == 1:
                twice = arr[i]
                

        miEle = 0
        for i in range(len(arr)):
            if miss[i] == 0:
                miEle = i+1
                break
                

        return [twice,miEle]
