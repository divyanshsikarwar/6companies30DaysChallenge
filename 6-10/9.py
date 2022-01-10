class Solution:
    def isValid(self, mat):
        # print(mat)
        d = set()
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j]>0:
                    box = (i//3)*3 + (j//3)
                    s1 = 'row' + str(i) + str(mat[i][j])
                    s2 = 'col' + str(j) + str(mat[i][j])
                    s3 = 'box' + str(box) + str(mat[i][j])
                    if s1 in d or s2 in d or s3 in d:
                        return 0
                    else:
                        d.add(s1)
                        d.add(s2)
                        d.add(s3)
                                
        return 1