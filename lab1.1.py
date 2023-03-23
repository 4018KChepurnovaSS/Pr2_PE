import numpy as np
import matplotlib.pyplot as plt

n = 50**3  # кол-во слотов
n_start = np.zeros(n, dtype=np.int64)  # количество абонентов начале
n_end = np.zeros(n, dtype=np.int64)  # количество абонентов в конце
M = [] # массив для среднего кол-ва аб
l_g = [] # массив λ для графика
t_g = [] # массив для среднего времени нахождения абонента в системе
for l in np.arange(0.01, 0.5, 0.01):  # распределение Пуассона
    l_g.append(l)
    P = np.random.poisson(l, n)
    
    for k in range(n - 1):  # цикл для подсчета кол-ва абонентов
        if n_start[k] != 0:
            R = np.random.binomial(n_start[k], 1 / n_start[k])
        else:
            R = 0

        if R == 1:
            I = 1
        else:
            I = 0
        n_end[k] = n_start[k] - I
        n_start[k + 1] = n_end[k] + P[k]
    # Среднее значение кол-ва абонентов в системе
    M.append(np.mean(n_end))
    n_start += n_end
    # Среднее значение времени нахождения аб в системе
    time = np.mean(n_end) / l
    t_g.append(time)
    
    #обнуление переменных 
    n_start = np.zeros(n, dtype=int)  
    n_end = np.zeros(n, dtype=int)  
    
#графики   
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.plot(l_g, M, color="red")

ax1.set_title('График зависимости среднего количества абонентов от λ')
ax1.set_ylabel('Среднее кол-во абонентов')
ax1.set_xlabel('Параметр λ')
plt.grid()
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.plot(l_g, t_g, color="purple")

ax2.set_title('График зависимости среднего времени нахождения абонента в системе от λ')
ax2.set_ylabel('Среднее время нахождения аб. в системе')
ax2.set_xlabel('Параметр λ')
plt.grid()
plt.show()