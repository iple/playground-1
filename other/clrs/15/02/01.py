import sys

sizes = [30, 35, 15, 5, 10, 20, 25]


def subscript(n):
    chars = "₀₁₂₃₄₅₆₇₈₉"
    result = []
    while n:
        rem = n % 10
        n //= 10
        result.append(chars[rem])

    return ''.join(reversed(result))


def order(dimensions):
    n = len(dimensions) - 1
    memo = [[-1] * n for _ in range(n)]
    choices = [[-1] * n for _ in range(n)]
    for i in range(0, n):
        memo[i][i] = 0

    for length in range(1, n):
        for start in range(0, n - length):
            end = start + length
            cheapest = sys.maxsize
            for split in range(start, end):
                cost = memo[start][split] + memo[split + 1][end] + \
                    dimensions[start] * dimensions[split + 1] * \
                    dimensions[end + 1]

                if cost < cheapest:
                    cheapest = cost
                    memo[start][end] = cost
                    choices[start][end] = split

    def optimal(i, j):
        if i == j:
            return "A" + subscript(i)
        else:
            left = optimal(i, choices[i][j])
            right = optimal(choices[i][j] + 1, j)
            return f"({left}{right})"

    return (memo[0][n - 1], optimal(0, n - 1))
