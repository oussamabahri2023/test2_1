def check_fit(side, w, h, n):
    return (side // w) * (side // h) >= n

def find_min_board_size(w, h, n):
    left = 0
    right = max(w, h) * n

    while left < right:
        mid = (left + right) // 2
        if check_fit(mid, w, h, n):
            right = mid
        else:
            left = mid + 1

    return left
w = int(input('Write the width of each diploma:'))
h = int(input('Write the height of each diploma:'))
n = int(input('Write the number of diplomas Petya has:'))

result = find_min_board_size(w, h, n)
print(result)