import csv

def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = [row for row in reader]
    return headers, rows

def extract_prices(rows):
    prices = []
    for row in rows:
        amount = row[1].replace('$', '')
        price = float(amount) if amount else 0.00
        prices.append(price)
    return prices

def find_product_by_price(rows, target_price):
    for row in rows:
        amount = row[1].replace('$', '')
        price = float(amount) if amount else 0.00
        if price == target_price:
            return row[0]
    return None