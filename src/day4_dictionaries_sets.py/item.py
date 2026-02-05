purchases={
    "Alice": 250,
    "Bob": 400,
    "Charlie":150

}
for customer, amount in purchases.items():
    print(f"{customer} made a purchase of ₹{amount}.")

    print("Total customers:", len(purchases))

    print("customers:", purchases.keys())