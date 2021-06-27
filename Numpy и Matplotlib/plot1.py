import matplotlib.pyplot as plt
import numpy as np
def line():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()
def line_point():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()
def styles():
    # # время равномерной выборки с интервалом 200 мс
    t = np.arange(0., 5., 0.2)
    #красные черточки, синие квадраты и зеленые треугольники
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.show()
#Работа с несколькими фигурами и осями
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
def paral_ex():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

def Annotating_text():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )

    plt.ylim(-2, 2)
    plt.show()
def log_axes():
    import numpy as np
    import matplotlib.pyplot as plt

    from matplotlib.ticker import NullFormatter  # useful for `logit` scale

    # фиксация seed
    np.random.seed(19680801)

    # произвольные числа на [0,1]
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    # plot with various axes scales
    plt.figure(1)

    # linear
    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)

    # log
    plt.subplot(222)
    plt.plot(x, y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)

    # symmetric log
    plt.subplot(223)
    plt.plot(x, y - y.mean())
    plt.yscale('symlog', linthreshy=0.01)
    plt.title('symlog')
    plt.grid(True)

    # logit
    plt.subplot(224)
    plt.plot(x, y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)

    plt.gca().yaxis.set_minor_formatter(NullFormatter())

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)

    plt.show()

plt.show()
line()
line_point()
styles()
paral_ex()
Annotating_text()
log_axes()