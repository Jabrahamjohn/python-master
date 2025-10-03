import matplotlib.pyplot as plt

# Data for the line graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting the graph
plt.plot(x, y, marker='o')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')

# Display the graph
plt.show()