L = [ 1, 6, 4, 99, 1, 2, 5, 3 ]

# ---------------------------------------------------

# def bubble_sort( items_input ):
#     items = items_input[:]
#     length = len(items_input)

#     for item_index_outter in range( length - 1 ):
#         did_we_swap = False
#         for item_index_inner in range( length - 1 - item_index_outter ):            # ВІДКИДАЄМО ВЖЕ ВІДСОРТОВАНИЙ ХВІСТ
#             if items[item_index_inner] > items[item_index_inner + 1]:
#                 items[item_index_inner], items[item_index_inner + 1] = items[item_index_inner + 1], items[item_index_inner]
#                 did_we_swap = True
#         if not did_we_swap:
#             break

#     return items

# print( bubble_sort(L) )

# ---------------------------------------------------

# def selection_sort( items_input ):
#     items = items_input[:]
#     length = len(items_input)

#     for item_index_outter in range( length ):
#         minimal_index_value = item_index_outter
#         for item_index_inner in range( item_index_outter + 1, length ):
#             if items[item_index_inner] < items[minimal_index_value]:
#                 minimal_index_value = item_index_inner
#         items[item_index_outter], items[minimal_index_value] = items[minimal_index_value], items[item_index_outter]

#     return items

# print( selection_sort(L) )

# ---------------------------------------------------
L = [ 1, 6, 4, 99, 1, 2, 5, 3 ]

def merge_sort( items ):
    print( f"merge_sort - start: {items}" )
    if len( items ) <= 1:
        return items

    items_middle = len( items ) // 2
    left = merge_sort( items[:items_middle] )
    right = merge_sort( items[items_middle:] )
    return merge( left, right )

def merge(left, right):
    print( f"merge - start: {left} + {right}" )
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    print( f"merge - end: {left} + {right} == {result}" )
    return result

print( merge_sort(L), L )
