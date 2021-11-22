from get_csv_shares import get_shares
from optimized import greedy

if __name__ == "__main__":
    shares = get_shares('data/dataset1.csv')
    shares2 = get_shares('data/dataset2.csv')
    print('///dataset1///')
    print(greedy(shares))
    print('///dataset2///')
    print(greedy(shares2))
