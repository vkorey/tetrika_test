def main(array):
    """
    >>> main("111111111110000000000000000")
    11
    >>> main("1000000000000000000000000000000000000000")
    1
    >>> main("111111111111111111111111110")
    26
    >>> main("1111110000000000000000")
    6
    """
    low = 0
    high = int(len(array)) - 1
    mid = int(len(array)) // 2
    while array[mid - 1] != 0 and low < high:
        if int(array[mid]) == 1:
            low = mid + 1
        elif int(array[mid]) == 0:
            high = mid
        mid = (low + high) // 2
    print(mid)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
