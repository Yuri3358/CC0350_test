def fatorial(n: int) -> int:
    acc = 1
    for number in range(1, n+1):
        acc *= number
    return acc