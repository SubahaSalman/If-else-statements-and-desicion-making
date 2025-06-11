ActualCost= float(input("Please enter the actual cost of the product: "))
SaleCost= float(input("Please enter the sale cost of the product: "))

Profit = SaleCost - ActualCost
if SaleCost<ActualCost:
    print("Your loss is ", Profit)
else: 
    print("Your profit is ", Profit)