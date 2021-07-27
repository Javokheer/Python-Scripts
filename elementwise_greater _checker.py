def elementwise_greater_than(L, thresh):
    """
    :param L: single integer
    :param thresh: list of integers
    :return: list of boolean values corresponding to each element in the list

    >>> elementwise_greater_than([3, 4, 5, 1], 3)
    [False, True, True, False]
    """

    return [i > thresh for i in L]

test = elementwise_greater_than([1, 2, 3, 4], 2)
print(test)

