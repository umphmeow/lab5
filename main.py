import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import timeit
import math
max_recursion_depth = 3000 # Максимальная глубина рекурсии
memory_F = {1: 1}
def F_recu(n):
    if n in memory_F:
        return memory_F[n]
    else:
        memory_F[n] = np.sin(F_recu(n - 1)) - G_recu(n - 1)
        return memory_F[n]

memory_G = {1: 1}
memory_fact = {1: 1}
def G_recu(n):
    if n in memory_G:
        return memory_G[n]
    else:
        F_n_1 = F_recu(n - 1)
        if n-1 in memory_fact:
            factorial = memory_fact[n - 1]
        else:
            factorial = math.factorial(n - 1)
            memory_fact[n - 1] = factorial
        memory_G[n] = 2 * F_n_1 - factorial
        return memory_G[n]

def F_iter(n):
    # Инициализируем массивы F и G
    F = [0] * (n+1)
    G = [0] * (n+1)
    F[1] = G[1] = 1

    # Вычисляем значения F и G для всех n от 2 до n
    for i in range(2, n+1):
        F[i] = np.sin(F[i-1]) - G[i-1]
        G[i] = 2*F[i-1] - math.factorial(i-1)

    return F[n]

n_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]



recursive_times = []
iterative_times = []
for n in n_values:

    recursive_time = timeit.timeit(lambda: F_recu(n), number=1)
    recursive_times.append(recursive_time)

    iterative_time = timeit.timeit(lambda: F_iter(n), number=1)
    iterative_times.append(iterative_time)

    print("n = {}, F_recursive({}) = {}, G_recursive({}) = {}, time = {:.8f} seconds".format(n, n, F_recu(n), n, G_recu(n), recursive_time))
    print("n = {}, F_iterative({}) = {}, time = {:.8f} seconds".format(n, n, F_iter(n), iterative_time))
    print()

data = {'n': n_values, 'recursive_time': recursive_times, 'iterative_time': iterative_times}
df = pd.DataFrame(data)

print(df)

plt.plot(n_values, recursive_times, 'ro', label='Recursive')
plt.plot(n_values, iterative_times, 'bo', label='Iterative')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time for calculating F(n)')
plt.legend()
plt.show()
