# For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. 
# That is, you need to print in the order followed for every iteration:

from sys import stdin


def spiralPrint(mat, nRows, mCols):
    # #Your code goes here
    # loop = nRows
    # if loop % 2 != 0:
    #     loop += 1
    # for i in range(loop//2):
    #     for j in range(i, mCols-i):
    #         print(mat[i][j], end=" ")
    #     for k in range(1+i, nRows-i):
    #         print(mat[k][j], end=" ")
    #     for l in range(mCols-2-i, -1+i, -1):
    #         print(mat[k][l], end=" ")
    #     for p in range(nRows-2-i, 0+i, -1):
    #         print(mat[p][l], end=" ")
    rs = 0
    re = nRows
    cs = 0
    ce = mCols
    while rs<re and cs<ce:

        for i in range(cs,ce):
            print(mat[rs][i],end=' ')
        rs+=1
        for i in range(rs,re):
            print(mat[i][ce-1],end=' ')
            # count-=1
        ce-=1
        if rs<re:
            for i in range(ce-1,cs-1,-1):
                print(mat[re-1][i],end=' ')
                # count-=1
            re-=1
        if cs<ce:
            for i in range(re-1,rs-1,-1):
                print(mat[i][cs],end=' ')
                # count-=1
            cs+=1    
    return


#Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0:

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
