import matplotlib.pyplot as plt
import numpy as np

# простой текстовый
plt.subplot(221)
plt.title('alpha > beta')
plt.grid(True)

# математический текст
plt.subplot(222)
plt.title(r'$\alpha > \beta$')
plt.grid(True)

plt.subplot(223)
plt.title(r'$\alpha_i > \beta_i$')
plt.grid(True)

plt.subplot(224)
plt.title(r'$\sum_{i=0}^\infty x_i$')
plt.grid(True)
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.55,wspace=0.35)
plt.show()

#########
#########
#########

plt.subplot(221)
plt.title(r'$\frac{5 - \frac{1}{x}}{4}$')
plt.grid(True)

plt.subplot(222)
plt.title(r'$\sqrt{2}$')
plt.grid(True)

plt.subplot(223)
plt.title(r'$\sqrt[3]{x}$')
plt.grid(True)

plt.subplot(224)
plt.title('s(t) = \mathcal{A}\/\sin(2 \omega t)')
plt.grid(True)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.94, hspace=0.55,wspace=0.35)
plt.show()

#########
#########
#########
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)

plt.plot(t,s)
plt.title(r'$\alpha_i > \beta_i$', fontsize=20)
plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=20)
plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',
         fontsize=20)
plt.xlabel('time (s)')
plt.ylabel('volts (mV)')
plt.show()