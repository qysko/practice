from random import randint
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

M, N = 30 , 30
k = 3

def rand_matr(M, N):
    return np.random.randint(0, 2, (M, N))
matr_M = np.array(rand_matr(M, N))#массив для теущего состояния

def iterate_numpy(matr_M,N,M):
    next_matr_M = np.zeros((N,M), dtype=np.int32)  # массив для следующего состояния
    res=[]
    for x in range(1, M - 1):
        for y in range(1, N - 1):
            count = 0  # кол-во соседей
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if matr_M[j][i]:
                        count += 1

            if matr_M[y][x]:  # если клетка была изначально жива
                count -= 1
                if count == 2 or count == 3:
                    next_matr_M[y][x] = 1
                    res.append((x,y))
            elif count == 3:
                next_matr_M[y][x] = 1
                res.append((x,y))
            else: next_matr_M[y][x] = 0
    return np.array(next_matr_M),res

matr_res = matr_M
for i in range(k):
    matr_res, res = iterate_numpy(matr_res, M, N)


def Point(matr_M,M,N,k):
    fig, ax = plt.subplots()
    plt.title(fr'Число шагов = {k}',)
    my_cmap = matplotlib.colors.ListedColormap(['black', 'white'])
    for x in range(M + 1):
        for y in range(N + 1):
            ax.axhline(x, lw=2, color='k', zorder=1)
            ax.axvline(y, lw=2, color='k', zorder=1)
    ax.imshow(matr_M,interpolation='none', cmap=my_cmap, extent=[0, N, 0, M], zorder=0)
    plt.show()

def PointZero(res):
    next_matr_M = np.zeros((N, M), dtype=np.int32)  # массив для следующего состояния
    for i in res:
        next_matr_M[i[0]][i[1]]=1
    return next_matr_M
#print(PointZero(res))
Point(matr_M,M,N,0)
Point(PointZero(res),M,N,k)



