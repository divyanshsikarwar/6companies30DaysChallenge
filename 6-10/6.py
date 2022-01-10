class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        i = 0
        ans = []
        temp = []
        for i in range(k):
            if len(temp) == 0:
                temp.append(arr[i])
            elif arr[i]<temp[-1]:
                temp.append(arr[i])
            else:
                while len(temp)>0 and arr[i]>temp[-1]:
                    temp.pop()
                    
                temp.append(arr[i])
                
        ans.append(temp[0])
        
        i = 0
        for j in range(k,n):
            if arr[i]==temp[0]:
                temp.pop(0)
            i+=1
            if len(temp) == 0:
                temp.append(arr[j])
            elif arr[j]<temp[-1]:
                temp.append(arr[j])
                
            else:
                while len(temp)>0 and arr[j]>temp[-1]:
                    temp.pop()
                temp.append(arr[j])
            ans.append(temp[0])
            
        return ans