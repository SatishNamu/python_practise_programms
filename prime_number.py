a = int(input('enter a number:'))
for n in range(2, a):
    if n == 2:
        print(n,'is a prime number')
    is_prime = False
    if n > 2:
        for i in range(2,n):
            if n%i != 0:
                is_prime = True
            else:
                is_prime = False
                break
        if is_prime is True:
            print(n, 'is a prime number')
        else:
            print(n, 'is composite number')