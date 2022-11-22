# Question - Write a program to solve 0-1 knapsack problem using dynamic programming or branch and bound startegy
# -------------------------------------------------------------------------


## 0/1 KNAPSACK USING DYNAMIC PROGRAMMING

def knapsack(Capacity,wt,val,n):
    
    dp=[0 for i in range(Capacity+1)]
    #print("dp=",dp)
    for i in range(1,n+1):
        for w in range(Capacity,0,-1):
            if wt[i-1]<=w:
                dp[w]= max(dp[w],dp[w-wt[i-1]]+val[i-1])
                #print(dp[w],end=" ")
        #print()
    return dp[Capacity]
    
# driver code

val=[60,100,120]
wt=[10,20,30]
Capacity=50

n= len(val)
print("\nvalue and weights:")
for i in range(n):
    print(val[i]," ",wt[i])
print("The Knapsac capacity is:",Capacity)

print("The maximum profit is:",knapsack(Capacity,wt,val,n))