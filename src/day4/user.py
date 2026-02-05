n=int(input("Enter number of  customers: "))
user_purchases={}
for i in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for{name}: "))
    user_purchases[name]=amount
print("Customer Purchases:",user_purchases)

top_customers=max(user_purchases,key=user_purchases.get)
print("Top spending customer:",top_customers)

lowest_customers=min(user_purchases,key=user_purchases.get)
print("Lowest spending customer:",lowest_customers)