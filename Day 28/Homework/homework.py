num = int(input("Enter a number: "))

if num <= 1:
    print("This isn't prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("This is prime number")
    else:
        print("This isn't prime number")
