def binary_search(array, item):
    array.sort()
    low= 0
    high = len(array)-1

    while low < high:
        middle = (low + high) // 2

        if array[middle] == item:
            print(f'Array contains {item}')
            return True
        elif array[middle] < item:
            low = middle + 1
        elif array[middle] > item:
            high = middle - 1
    print(f"Array doesn't contain {item}")
    return False

binary_search([25, 27, 3, 36, 26, 20, 34, 46, 5, 31], 6)
