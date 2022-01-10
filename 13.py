
class Solution:
    def decodedString(self, s):

        newS = ''
        temp = ''
        st = []
        n = len(s)
        i=0
        while i<n:
            
            if s[i].isnumeric():
                t2 = ''
                while s[i].isnumeric():
                    t2 += s[i]
                    i+=1
        
                st.append(int(t2))
            if s[i] == '[':
                st.append('*')
                i+=1
            elif s[i] == ']':
                t1 = []
                while len(st)>0 and st[-1] != '*':
                    x = st.pop()
                    t1.append(x)
                st.pop()
                t1 = t1[::-1]
                t1 = ''.join(t1) 
                num = st.pop()
                t1 = t1*int(num)
                st.append(t1)
                i+=1
            else:
                st.append(s[i])
                i+=1
                
        return st[-1]
