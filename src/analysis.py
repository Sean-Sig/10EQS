if __name__ == "__main__":
    with open('data/products.txt', 'r') as f:
        headers = f.readline().strip().split(',')
        rows = [line.strip().split(',') for line in f]

    print("Headers:", headers)
    print("Data:", rows)