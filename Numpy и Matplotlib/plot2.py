import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

#############
######1######
#############
plt.title("sin cos")
plt.plot(C)
plt.plot(S)
plt.show()

#############
######2######
#############
plt.figure(figsize=(10,6), dpi=80)
plt.title("изменение цвета и толщины линий")
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-")
plt.show()

#############
######3######
#############
plt.title("изменение пределов")
plt.plot(X, C,)
plt.plot(X, S,)
plt.xlim (X.min () * 1.1, X.max () * 1.1)
plt.ylim (C.min () * 1.1, C.max () * 1.1)
plt.show()

#############
######4######
#############
plt.title("Установка меток")
plt.plot(X, C,)
plt.plot(X, S,)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
plt.show()

#############
######5######
#############
plt.title("смещение по оси")
plt.plot(X, C,)
plt.plot(X, S,)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()

#############
######6######
#############
plt.title("добавление легенды")
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.legend(loc='upper left', frameon=False)
plt.show()

#############
######7######
#############
plt.title("аннотирование моментов")
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.legend(loc='upper left', frameon=False)

t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()

#############
######8######
#############
# Новая фигура на белом фоне
fig = plt.figure(figsize=(6,6), facecolor='white')

# Новая ось по всей фигуре, без рамки и с соотношением сторон 1: 1
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)
# Количество
n = 50
size_min = 50
size_max = 50*50

#  Положение кольца
P = np.random.uniform(0,1,(n,2))

# Цвета колец
C = np.ones((n,4)) * (0,0,0,1)
# Цветовой канал альфа изменяется от 0 (прозрачный) до 1 (непрозрачный)
C[:,3] = np.linspace(0,1,n)

# Размер кольца
S = np.linspace(size_min, size_max, n)

# Точечная диаграмма
scat = ax.scatter(P[:,0], P[:,1], s=S, lw = 0.5,
                  edgecolors = C, facecolors='None')

# Убедитесь, что пределы равны [0,1], и удалите галочки
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])

def update(frame):
    global P, C, S

    # Каждое кольцо делается более прозрачным
    C[:,3] = np.maximum(0, C[:,3] - 1.0/n)

    # Каждое кольцо увеличивается
    S += (size_max - size_min) / n

    # Сбросить кольцо
    i = frame % 50
    P[i] = np.random.uniform(0,1,2)
    S[i] = size_min
    C[i,3] = 1

    # Обновить scatter object
    scat.set_edgecolors(C)
    scat.set_sizes(S)
    scat.set_offsets(P)

    return scat,

animation = FuncAnimation(fig, update, interval=10, blit=True, frames=200)
plt.show()