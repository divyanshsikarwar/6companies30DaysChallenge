class Solution:
    def printMinNumberForPattern(ob,s):
        arr = [0]*(len(s)+1)
        
        var = 1
        li = s.split('I')
        inde = []
        for i in range(len(s)):
            if s[i] == 'I':
                inde.append(i)
                
        inde.append(i+1)
        
        st = 0
        end = len(s)
        while len(inde)>0:
            index = inde.pop(0)
            while index>=st  and index<=end:
                if arr[index] == 0:
                    arr[index] = var
                    var+=1
                    index -= 1
                else:
                    break
                
        t1=  ''.join(str(x) for x in arr)
        return int(t1)
