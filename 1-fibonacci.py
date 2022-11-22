# Question - Write a program NON-RECURSIVE and RECURSIVE program to calculate Fibonacci numbers and analyze their time and space complexity
# -----------------------------------------------------------------------------



# NON-RECURSIVE(Iterative) program to calculate fibonacci ---------------------------------------
#  Time complexity - O(n)
#  Space Complexity - O(n) and O(1) if done by dynamic programming
import time

def fib_iterative(n):
    start=time.time()
    x=0
    y=1
    z=0    
    for i in range(n):
        print(x)
        z=x+y
        x=y
        y=z
    end=time.time()
    print("Time taken by non-recursive code:",end-start," sec")

n=int(input("Enter the number of elemnets to be generated: "))
print("The fibonacci series by iterative method is: ")
fib_iterative(n)


# RECURSIVE program to calculate fibonacci ------------------------------------------------------
#   Time Complexity - O(2^n)
#   Space Complexity - O(n)
def fibonacci(n):
    
    if n<=1:
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

print("The fibonacci series by recursive method is: ")
start=time.time()
i=1
for i in range(n):
    print(fibonacci(i))
end=time.time()
print("Time taken by recursive code:",end-start," sec")