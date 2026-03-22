import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Array:\n", arr)

arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])

print("Element at (0,1):", arr2[0, 1])
print("Row 1:", arr2[1, :])
print("Column 2:", arr2[:, 2])