from bisect import bisect_left, bisect_right


L = list( range( 1, 500_000 ) )

# O(n)
def linear_search( items, target ):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

# bin
def binary_search( items, target ):
    if not items:
        return -1

    left_index = 0
    right_index = len( items ) - 1

    while left_index <= right_index:
        target_index = ( left_index + right_index ) // 2
        if items[target_index] == target:
            return target_index
        elif items[target_index] < target:
            left_index = target_index + 1
        else:
            right_index = target_index - 1

    return -1


print(binary_search(L, 499_999))
print(bisect_left(L, 499_999))
print(bisect_right(L, 499_999))
