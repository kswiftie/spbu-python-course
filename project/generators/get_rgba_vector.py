def get_rgba_vector(i: int) -> tuple[int, int, int, int]:
    """
    A function that calculates the rgba color values of a vector by its ordinal number
    Parameters
    ----------
    i: int
        Number of vector that to be calculated
    Returns
    -------
    tuple[int, int, int, int]
        RGBA vecetor
    """
    generator = (
        (r, g, b, a)
        for b in range(256)
        for g in range(256)
        for r in range(256)
        for a in range(0, 101) if a % 2 == 0
    )
    try:
        for _ in range(i):
            next(generator)
        return next(generator)
    except Exception:
        raise ValueError("RGBA vector with such number does not exist")
