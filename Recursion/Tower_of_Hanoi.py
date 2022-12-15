#Tower of Hanoi
#Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. The objective of the puzzle is to move the entire stack to another rod (her


def tower(n,a,b,c):
    if n<=0:
        return
    tower(n-1,a,c,b)
    print(a,c)
    tower(n-1,b,a,c)

n=int(input())
tower(n, 'a', 'b', 'c')
