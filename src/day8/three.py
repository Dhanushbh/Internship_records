cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print("3D Data:")

for layer in cube:
    for row in layer:
        for val in row:
            print(val, end=" ")
        print()
    print("----")
