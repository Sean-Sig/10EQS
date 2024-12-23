import utils as util

if __name__ == "__main__":
    headers, rows = util.read_csv('data/products.csv')
    prices = util.extract_prices(rows)

    average_price = sum(prices) / len(prices)
    print("Average Price:", average_price)

    max_price = max(prices)
    min_price = min(prices)

    print("Max Price:", max_price)
    print("Min Price:", min_price)

    max_price_product = util.find_product_by_price(rows, max_price)
    min_price_product = util.find_product_by_price(rows, min_price)

    print("Product with Max Price:", max_price_product)
    print("Product with Min Price:", min_price_product)

    if min_price == 0.00:
        print(f"error: {min_price_product} product has a $0.00 price")