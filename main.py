import math
import pandas as pd
import matplotlib.pyplot as plt
import timeit

max_recursion_depth = 3000


memo_F = {1: 1}
def F_recu(n):
    if n in memo_F:
        return memo_F[n]
    else:
        memo_F[n] = math.sin(F_recu(n-1)) - G_recu(n-1)
        return memo_F[n]


memo_G = {1: 1}
memo_factorial = {1: 1}
def G_recu(n):
    if n in memo_G:
        return memo_G[n]
    else:
        F_n_1 = F_recu(n - 1)
        if n-1 in memo_factorial:
            factorial_n_1 = memo_factorial[n-1]
        else:
            factorial_n_1 = math.factorial(n - 1)
            memo_factorial[n-1] = factorial_n_1
        memo_G[n] = 2*F_n_1 - factorial_n_1
        return memo_G[n]


memo_F_iter = {1: 1}
memo_G_iter = {1: 1}
memo_factorial_iter = {1: 1}

def F_iter(n):
    if n in memo_F_iter:
        return memo_F_iter[n]
    else:
        F_n = F_iter(n - 1) if n - 1 in memo_F_iter else math.sin(F_iter(n - 1)) - G_iter(n - 1)
        memo_F_iter[n] = F_n
        G_n = G_iter(n - 1) if n - 1 in memo_G_iter else 2 * F_iter(n - 1) - math.factorial(n - 1)
        memo_G_iter[n] = G_n
        return F_n

def G_iter(n):
    if n in memo_G_iter:
        return memo_G_iter[n]
    else:
        F_n_1 = F_iter(n - 1) if n-1 in memo_F_iter else math.sin(F_iter(n-1)) - G_iter(n-1)
        memo_F_iter[n-1] = F_n_1
        if n-1 in memo_factorial_iter:
            factorial_n_1 = memo_factorial_iter[n-1]
        else:
            factorial_n_1 = math.factorial(n - 1)
            memo_factorial_iter[n-1] = factorial_n_1
        memo_G_iter[n] = 2*F_n_1 - factorial_n_1
        return memo_G_iter[n]

print("Программа вычисляет значение функции F для каждого введеного n двумя способами рекурсивно и итерационо: F(n) = sin(F(n–1)) – G(n–1),где G(n) = 2*F(n–1) - (n–1)!")

n_values = input("Введите значения n через пробел, не превышающие 171: ").split()
n_values = [int(n) for n in n_values if n.isdigit() and 1 <= int(n) <= 200]

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
    plt.plot(n_values, recursive_times, label='Recursive')
    plt.plot(n_values, iterative_times, label='Iterative')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Time for calculating F(n)')
    plt.legend()
    plt.show()
