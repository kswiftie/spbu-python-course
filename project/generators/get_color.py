def rgba_vector_gen(i):
    # todo: add description and exception to max i (if vector with number i does not exist)
    generator = (
        (r, g, b, a)
        for b in range(256)
        for g in range(256)
        for r in range(256)
        for a in range(0, 101, 2)
    )
    for _ in range(i):
        next(generator)
    return next(generator)
