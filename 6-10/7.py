class Solution:
    def FirstNonRepeating(self, s):
        st = []
        arr = [0]*26
        ans = ''
        
        for i in range(len(s)):
            flag = False
            temp = ord(s[i]) - 97
            arr[temp] += 1
            if arr[temp] == 1:
                st.append(s[i])
            
            while len(st)>0 and flag == False:
                if arr[ord(st[0]) - 97] == 1:
                    flag = True
                    ans += st[0]
                else:
                    st.pop(0)
            if flag == False:
                ans+='#'
                
        return ans