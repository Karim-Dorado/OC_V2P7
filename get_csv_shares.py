from csv import DictReader

"""Convert a csv file into a list of dictionaries"""
def get_shares(file):
    shares = []
    with open(file, 'r', encoding='utf8') as my_file:
        csv_reader = DictReader(my_file)
        for row in csv_reader:
            if round(float(row['price']), 2) >= 0.001:
                shares.append(row)
            else:
                pass
    return shares