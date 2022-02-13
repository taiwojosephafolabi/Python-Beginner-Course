# Plotting Graphs
# First import module
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
# plt.plot(x)
# plt.show()

y = [1, 8, 27, 64]
# plt.plot(x,y)
# plt.show()

# Plotting with colours
x = [1, 7, 12]
y = [6, 23, 31]
plt.plot(x, y, c="red", linewidth=2, label="Line 1")
# plt.show()

x2 = [5, 9, 15]
y2 = [10, 27, 40]
plt.plot(x2, y2, c="green", linewidth=0.5, label="Line 2")
# plt.show()

# Label axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the legend on the plot
plt.legend()
# plt.show()

# Extras
x = [1, 7, 12]
y = [6, 23, 31]
plt.plot(x, y, c="red", linewidth=2, label="Line 1")

x2 = [5, 9, 15]
y2 = [10, 27, 40]
plt.plot(x2, y2, c="green", linewidth=2, label="Line 2", linestyle="dashed", marker="o", markerfacecolor="orange",
         markersize=10)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.xlim(1, 20)
plt.ylim(1, 50)
plt.show()
