def algorithm(n):
    last_char = None
    len = 0
    longest_len = 0

    for c in n:
        if last_char is None:
            len += 1
        elif c == last_char:
            len += 1
        elif c != last_char:
            longest_len = max(longest_len, len)
            len = 1

        last_char = c
    return max(longest_len, len)


def main():
    n = str(input())
    print(algorithm(n))


if __name__ == "__main__":
    main()
