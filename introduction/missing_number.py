def algorithm(n, numbers):
    numbers = set(numbers)
    others = set(range(1, n + 1))
    return list(others - numbers)[0]


def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(algorithm(n, numbers))


if __name__ == "__main__":
    main()
