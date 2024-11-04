def gcd(m, n):
     while m != 0:
         m, n = n % m, m 
         return n 
m = int(input("Enter the first number: ")) 
n = int(input("Enter the second number: "))
print(f"The GCD of {m} and {n} is {gcd(m, n)}")
