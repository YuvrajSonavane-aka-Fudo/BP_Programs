def nonPrime(n):
    n = abs(n)
    for i in range(2,n):
        if n%i== 0:
            return "Not Prime"
    return "Prime"

print(nonPrime(23))




