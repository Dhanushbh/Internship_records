contacts = {
    "Rahul": "9876543210",
    "Anita": "9123456780",
    "Kiran": "9000012345"
}

# Add a new contact
contacts["Neha"] = "8899776655"

# Update an existing contact
contacts["Anita"] = "9012345678"

# Safe access using .get()
print("Lookup Rahul:", contacts.get("Rahul", "Contact not found"))
print("Lookup Suresh:", contacts.get("Suresh", "Contact not found"))

print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
