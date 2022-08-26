n = int(input('enter a number:'))
for i in range(1,n+1):
    odd_number = i*2-1
    print(' ' * (n-i), '*' * odd_number)
for j in range(n-1,0,-1):
    odd_number = j*2-1
    print(' '* (n-j), '*' * odd_number)