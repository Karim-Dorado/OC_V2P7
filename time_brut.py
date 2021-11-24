from brutforce import brutforce
from get_csv_shares import get_shares
import matplotlib.pyplot as plt
from timeit import timeit

"""
Will generate a graph which give us the execution time of the brutforce algorithm
in function of number of shares
"""
nb_shares = []
execution_time = []
shares = get_shares('data/brutforce.csv')
for i in range(2,21):
    nb_shares.append(i)
    shares_list = shares[0:i]
    execution_time.append(timeit(stmt= 'brutforce(shares_list)', setup='', number=1, globals=globals()))
plt.plot(nb_shares,execution_time)
plt.xlabel("nombre d'actions")
plt.ylabel("temps d'execution en s")
plt.title("temps d'execution en fonction du nombre d'actions")
plt.show()