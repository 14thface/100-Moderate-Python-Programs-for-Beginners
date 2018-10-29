number = input('What is your number? -')
n = int(number) #converting the string to integer

if n > 1: #to avoid slips if the input is 1
    for i in range(2, n):
        if (n % i) == 0:
            print(n,' is not a prime number.')
            print(i,'x',n//i,'=',n)
            #to break the loop from running all the n times
            break

        else:
            print('{} is a Prime Number.' . format(n))

else:
    print('{} is a Prime Number.' . format(n))
