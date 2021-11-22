from get_csv_shares import get_shares
from itertools import combinations

def brutforce(shares):
    res = {'shares': [],'price': 0,'gains': 0, 'profit': 0}
    for i in range(2, len(shares)+1):
        for combination in combinations(shares, i):
            prices = [float(share['price']) for share in combination]
            price = sum(prices)
            if price <= 500:
                shares_list = [share['name'] for share in combination]
                gains = sum([(float(share['price']) * float(share['profit']))/100 for share in combination])
                profit = ((((price+gains) - price)/price)*100)
                if gains > res['gains']:
                    res = {
                        'shares':shares_list,
                        'price': price,
                        'gains': round(gains, 2),
                        'profit': round(profit, 2)
                        }
                    with open('brutforce_profit.txt', 'w', encoding='utf8') as f:
                        f.write(str(res))
    return res

if __name__ == "__main__":
    shares = get_shares('data/brutforce.csv')
    print(brutforce(shares))
