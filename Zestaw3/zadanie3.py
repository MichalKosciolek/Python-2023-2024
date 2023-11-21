import matplotlib.pyplot as plt
import numpy as np

x_min = int(input('x_min: '))
x_max = int(input('x_max: '))
x_val = np.linspace(x_min, x_max, 200)

print('f(x) = ', end='')
fx = input()
y_val = [eval(fx) for x in x_val]

plt.plot(x_val, y_val)
plt.title('Wykres wielomianu')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()