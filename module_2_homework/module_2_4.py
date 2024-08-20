numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    for k in range(1, len(numbers)):
        if i%k == 0 and (k != 1 and k != i):
            not_primes.append(i)
            break
    else:
        if i != 1:
            primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)
