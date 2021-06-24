import numpy as np

def input_make():
    lst=[]
    grid=[]
    for i in range(9):
        for j in range(9):
            q=input("x {} y좌표: {} 를 입력하세요".format(j+1,i+1))
            lst.append(int(q))
        grid.append(lst)
        lst=[]
    return grid

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range(0,9):
        if grid[i][x]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid [y0+i][x0+j]==n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        if grid[y][x]==0:
                            grid[y][x]=n
                            solve()
                            grid[y][x]=0
                return
    print(np.matrix(grid))
    input("more?")            

#main
grid=input_make()
print(np.matrix(solve()))
