def find_max_two(arr: list[int]) -> list[int]:
    """ Find the two largest numbers in a list.
    Args:
        arr (list[int]): A list of integers.
    Returns:
        list[int]: A list containing the two largest integers.
    """
    if len(arr) < 2:
        return arr

    max1, max2 = arr[:2]
    if max1 < max2:
        max1, max2 = max2, max1
    for n in arr[2:]:
        if n > max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n
    return [max1, max2]


# Test cases
arr = [[3, -1, 5, 0, 7, 4, 9, 1], [7]]
for a in arr:
    print(f"Input: {a}, Output: {find_max_two(a)}")
