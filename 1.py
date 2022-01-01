   def Anagrams(self, words, n):
       d = {}
       for i in words:
           s = ''.join(sorted(i))
           try:
               d[s].append(i)
           except:
               d[s]=[i]
           
       ret = []
       for i in d:
           ret.append(d[i])
       return ret
        #code here
