def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)

    result_first = tuple_a[0] + tuple_b[0]
    result_second = tuple_a[1] + tuple_b[1]

    return (result_first, result_second)
