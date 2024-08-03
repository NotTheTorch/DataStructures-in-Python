def sum_N(num):
    sum = 0
    if num < 1:
        return 0
    return num + sum_N(num-1)

def main():
    N = 5
    print(sum_N(N))


if __name__ == "__main__":
    main()