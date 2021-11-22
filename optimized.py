from get_csv_shares import get_shares

def greedy(shares):
    res = {'shares': [],'price': 0,'gains': 0, 'profit': 0}
    limit = 500
    list_shares = sorted(shares, key=lambda x: float(x['profit']), reverse=True)
    for share in list_shares:
        if float(share['price']) <= limit:
            limit -= float(share['price'])
            res['shares'].append(share['name'])
            res['price'] += float(share['price'])
            res['gains'] += (float(share['price']) * float(share['profit']))/100
            res['profit'] = round(((((res['price'] + res['gains']) - res['price']) / res['price'])*100), 2)
            res['price'] = round(res['price'], 2)
            res['gains'] = round(res['gains'], 2)
    return res


if __name__ == "__main__":
    shares = get_shares('data/brutforce.csv')
    print(greedy(shares))
