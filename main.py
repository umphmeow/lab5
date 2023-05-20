import math
import pandas as pd
import matplotlib.pyplot as plt
import timeit

memory_F = {1: 1}
def F_recu(n):
    if n in memory_F:
        return memory_F[n]
    else:
        memory_F[n] = math.sin(F_recu(n - 1)) - G_recu(n - 1)
        return memory_F[n]


memory_G = {1: 1}
memory_factorial = {1: 1}
def G_recu(n):
    if n in memory_G:
        return memory_G[n]
    else:
        F_n_1 = F_recu(n - 1)
        if n-1 in memory_factorial:
            factorial_n_1 = memory_factorial[n - 1]
        else:
            factorial_n_1 = math.factorial(n - 1)
            memory_factorial[n - 1] = factorial_n_1
        memory_G[n] = 2 * F_n_1 - factorial_n_1
        return memory_G[n]


def F_iter(n):
    F_1 = F_2 = 1
    G_1 = G_2 = 1

    for i in range(2, n+1):
        F = math.sin(F_1) - G_1
        G = 2*F_1 - math.factorial(i-1)

        F_2, F_1 = F_1, F
        G_2, G_1 = G_1, G

    return F

print("Программа вычисляет значение функции F для каждого введеного n двумя способами рекурсивно и итерационо: F(n) = sin(F(n–1)) – G(n–1),где G(n) = 2*F(n–1) - (n–1)!")

n_values = input("Введите значения n через пробел, не превышающие 171, но больше 0: ").split()
n_values = [int(n) for n in n_values if n.isdigit() and 1 <= int(n) <= 173]

if len(n_values) == 0:
    print("Вы не ввели корректные значения n.")
else:
    recursive_times = []
    iterative_times = []
    for n in n_values:
        recursive_time = timeit.timeit(lambda: F_recu(n), number=100)
        recursive_times.append(recursive_time)
        iterative_time = timeit.timeit(lambda: F_iter(n), number=100)
        iterative_times.append(iterative_time)

    data = {'n': n_values, 'recursive_time': recursive_times, 'iterative_time': iterative_times}
    df = pd.DataFrame(data)

    # Выводим таблицу на экран
    print(df)

    # Строим график зависимости времени выполнения от значения n
    plt.plot(n_values, recursive_times, 'ro', label='Recursive')
    plt.plot(n_values, iterative_times, 'bo', label='Iterative')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Time for calculating F(n)')
    plt.legend()
    plt.show()
