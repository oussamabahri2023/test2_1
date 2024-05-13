def min_weight_difference(N, weights):
    total_weight = sum(weights)
    min_diff = float('inf')
    diff_list = []
    if not 1 <= N <= 18:
        print("N is not between 1 and 18")
    for i in range(1, 2 ** N):
        pile_weight = 0
        for j in range(N):
            if i & (1 << j):
                pile_weight += weights[j]
        diff = abs(total_weight - 2 * pile_weight)
        min_diff = min(min_diff, diff)
        diff_list.append(min_diff)

    return list(set(diff_list))

N = int(input('Write the numbers of stones: '))
weights = input('Write the weights of the stones separated by comma: ').split(',')
weights = [int(i) for i in weights]
result = min_weight_difference(N, weights)
print('The result is:', result)

