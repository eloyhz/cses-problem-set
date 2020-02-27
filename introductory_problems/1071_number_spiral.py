def spiral(yi, xi):
    n = max(yi, xi)
    if n % 2 == 0:
        if yi <= xi:
            return (n - 1) * (n - 1) + yi
        else:
            return n * n - (xi - 1)
    else:
        if xi <= yi:
            return (n - 1) * (n - 1) + xi
        else:
            return n * n - (yi - 1)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        y, x = map(int, input().split())
        print(spiral(y, x))

