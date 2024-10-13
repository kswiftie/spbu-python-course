import functools


def get_prime_number(gen):
    # todo: add description and exceptions
    @functools.wraps(gen)
    def inner(n):
        s = gen
        for i in range(n - 1):
            next(s)
        return next(s)

    return inner


def prime_seq_gen(stopnumber=1000):
    # todo: add description and exceptions
    prime_numbers = [2]
    yield 2
    for n in range(3, stopnumber + 1):
        is_prime = True
        for p in prime_numbers:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(n)
            yield n
