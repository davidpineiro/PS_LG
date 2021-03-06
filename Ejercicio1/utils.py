import itertools
import functools
import operator

def prime_generator(n):
    """
    Sieve of Eratosthenes
    Create a candidate list within which non-primes will be
    marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * (
                    (n // cand[i]) - (n // (2 * cand[i])) - 1)

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


def factorize(n, primes_list):
    prime_multiples = []
    for item in primes_list:
        if item > n:
            break
        else:
            while n > 1:
                if n % item == 0:
                    n //= item
                    prime_multiples.append(item)
                else:
                    break
    return prime_multiples


def calculate_divisors(n, primes_list):
    prime_multiples_list = factorize(n, primes_list)

    """
    construct unique combinations
    A, B, B, C --> A, B, C, AB, AC, BB, BC, ABC, ABB, BBC
    """
    unique_combinations = set()
    for i in range(1, len(prime_multiples_list)):
        unique_combinations.update(
            set(itertools.combinations(prime_multiples_list, i)))

    # multiply elements of each unique combination
    combination_product = list(functools.reduce(operator.mul, i)
                               for i in unique_combinations)
    combination_product.sort()

    # add the element 1 as the first divisor
    combination_product.insert(0, 1)

    return combination_product
