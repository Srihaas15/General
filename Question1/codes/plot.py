import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libcalculate_p.so')

# Set argument and return types
lib.calculate_p.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double * 10)]

# Prepare variables
p = ctypes.c_double(0.0)
points_array_type = ctypes.c_double * 10  # 5 points * 2 coordinates
points = points_array_type()

# Call the C function to calculate p and generate points
lib.calculate_p(ctypes.byref(p), points)

# Convert points to a NumPy array for plotting
points_list = np.array([[points[i * 2], points[i * 2 + 1]] for i in range(5)])

# Original points
original_points = np.array([[2, 1], [p.value, -1], [-1, 3]])

# Plotting
plt.figure(figsize=(8, 6))

# Plot the segment from (-1, 3) to (2, 1)
plt.plot([2, -1], [1, 3], label='Line from (-1, 3) to (2, 1)', color='blue', marker='o')

# Plot the segment from (2, 1) to (p, -1)
plt.plot([2, p.value], [1, -1], label='Line from (2, 1) to (p, -1)', color='green', marker='o')

# Scatter the original points
plt.scatter(original_points[:, 0], original_points[:, 1], color='red')

# Label the points
plt.annotate('(-1, 3)', xy=(-1, 3), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate('(2, 1)', xy=(2, 1), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(f'({p.value:.2f}, -1)', xy=(p.value, -1), textcoords="offset points", xytext=(0,10), ha='center')

# Set limits for better visualization
plt.xlim(-2, 5)
plt.ylim(-2, 4)

plt.title('Collinear Points and Intermediate Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5, ls='-')
plt.axvline(0, color='black', linewidth=0.5, ls='-')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('../figs/fig.png')
plt.show()

