import math_operation
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

nums = input("Enter numbers separated by space: ")
numbers_list = list(map(int, nums.split()))

p = math_operation.power(base, exp)
avg = math_operation.average(numbers_list)

print("Power result:", p)
print("Average:", avg)