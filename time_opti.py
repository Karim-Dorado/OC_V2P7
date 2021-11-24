from timeit import timeit
from optimized import greedy
from main import get_shares
import matplotlib.pyplot as plt

"""
Will generate a graph which give us the execution time of the optimized algorithm
in function of the number of shares
"""
nb_shares = [500,600,700,800,957]
execution_time = []
for value in nb_shares:
    shares_list = get_shares('data/dataset1.csv')[0:value]
    execution_time.append(timeit(stmt= 'greedy(shares_list)', setup='', number=1, globals=globals()))

plt.plot(nb_shares,execution_time)
plt.xlabel("nombre d'actions")
plt.ylabel("temps d'execution en ms")
plt.title("temps d'execution en fonction du nombre d'actions")
plt.show()