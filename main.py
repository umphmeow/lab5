import math
import pandas as pd
import matplotlib.pyplot as plt
import timeit

# Определяем границы применимости рекурсивного и итерационного подходов
max_recursion_depth = 3000 # Максимальная глубина рекурсии
max_memory_usage = 1000000 # Максимальный объем памяти (в байтах)

# Функция для вычисления значения функции F(n) рекурсивно с memo
memo_F = {1: 1}
def F_recu(n):
    if n in memo_F:
        return memo_F[n]
    else:
        memo_F[n] = math.sin(F_recu(n-1)) - G_recu(n-1)
        return memo_F[n]

# Функция для вычисления значения функции G(n) рекурсивно с memo
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

# Функция для вычисления значения функции F(n) итерационно
def F_iter(n):
    # Инициализируем массивы F и G
    F = [0] * (n+1)
    G = [0] * (n+1)
    F[1] = G[1] = 1

    # Вычисляем значения F и G для всех n от 2 до n
    for i in range(2, n+1):
        F[i] = math.sin(F[i-1]) - G[i-1]
        G[i] = 2*F[i-1] - math.factorial(i-1)

    return F[n]

print("Программа вычисляет значение функции F для каждого введеного n двумя способами рекурсивно и итерационо: F(n) = sin(F(n–1)) – G(n–1),где G(n) = 2*F(n–1) - (n–1)!")

n_values = input("Введите значения n через пробел, не превышающие 171: ").split()
n_values = [int(n) for n in n_values if n.isdigit() and 1 <= int(n) <= 171]

if len(n_values) == 0:
    print("Вы не ввели корректные значения n.")
else:
    # Вычисляем значения функций F(n) и G(n) с помощью timeit
    recursive_times = []
    iterative_times = []
    for n in n_values:
        recursive_time = timeit.timeit(lambda: F_recu(n), number=100)
        recursive_times.append(recursive_time)
        iterative_time = timeit.timeit(lambda: F_iter(n), number=100)
        iterative_times.append(iterative_time)

    # Сохраняем результаты вычислений в таблицу
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
