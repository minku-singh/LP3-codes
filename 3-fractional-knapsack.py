# Question - Write a program to solve fractional knapsack problem using greedy method
# -------------------------------------------------------------------------------


#Fractional Knapsack using greedy method

class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        
def fractionalknapsack(Capasity,arr):
    
    arr.sort(key=lambda x:(x.value/x.weight),reverse= True)
    
    finalvalue=0.0
    
    for item in arr:
        
        if item.weight <Capasity:
            Capasity -= item.weight
            finalvalue += item.value
            
        else:
            finalvalue += item.value*(Capasity/item.weight)
            
            break
            
    return finalvalue
 
#Driver code

if __name__=="__main__":
    
    capacity=50 # Capasity of Knapsack, the maximum items can be put in bag
    arr=[Item(60,10),Item(100,20),Item(120,30)]
    
    print("\nvalue and weights:")
    for i in range(len(arr)):
        print(arr[i].value," ",arr[i].weight)
    print("The Knapsac capacity is:",capacity)
    
    max_value=fractionalknapsack(capacity,arr)
    print("The maximum profit is:",max_value)