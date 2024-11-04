def fibonacci(n): 
    if n <= 0:
         return "Input must be a positive integer" 
    elif n == 1:
         return 1 
    elif n == 2: 
        return 1 
    else: 
        a, b = 1, 1 
        for _ in range(3, n+1):
             a, b = b, a + b 
             return b 
n = int(input("Enter the value of n: "))
 print(f"The {n}th Fibonacci number is {fibonacci(n)}")
main()