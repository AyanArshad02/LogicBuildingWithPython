def is_prime(num):
    if num <= 1:
        return "Not a Prime Number"
    
    for i in range(2,num):
        if num % i == 0:
            return "Not a Prime Number"
        
    return "Prime Number"

n = int(input("Enter a number: "))
result = is_prime(n)

print(f"{n} is {result}")
