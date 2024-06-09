
def bin_fib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return bin_fib(n-1) + bin_fib(n-2)


def lin_fib(n):
    if n <= 1:
        return (0, 0)
    if n == 2:
        return (1, 0)
    pre, prepre = lin_fib(n-1)
    return (pre+prepre, pre)


def main():
    n = int(input("Unesi broj: "))
    print(f"{n}-ti fibonacijev broj je {bin_fib(n)}")
    print(f"{n}-ti fibonacijev broj je {lin_fib(n)[0]}")


if __name__ == "__main__":
    main()