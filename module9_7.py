def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)

        def if_prime(n):
            if n == 2 or n == 3: return True
            if n < 2 or n % 2 == 0: return False
            if n < 9: return True
            if n % 3 == 0: return False
            r = int(n ** 0.5)
            f = 5
            while f <= r:
                print('\t', f)
                if n % f == 0: return False
                if n % (f + 2) == 0: return False
                f += 6
            return True
        if n==1:
            print(f'Число {n} не является ни составным, ни простым')
            return n
        else:
            if if_prime(n):
                print(f'Число {n} простое')
            else:
                print(f'Число {n} составное')
            return n

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(1, 10, 15))
