def isPrime(n):
    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

a = []

for i in range(2, n + 1):
    if isPrime(i):
        a.append(i)

print(a)