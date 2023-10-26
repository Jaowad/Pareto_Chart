import matplotlib.pyplot as plt

# Sample data (replace with your own)
categories = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I']
Value = [10, 8, 6, 4, 2,3,5,2,6]

# Calculate cumulative frequency
cumulative_frequency = [sum(Value[:i+1]) for i in range(len(Value))]

# Create the Pareto chart
fig, ax1 = plt.subplots()

# Create the bar chart
ax1.bar(categories, Value, color='b')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Frequency', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create the line plot
ax2 = ax1.twinx()
ax2.plot(categories, cumulative_frequency, color='r')
ax2.set_ylabel('Cumulative Frequency', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add title and show the plot
plt.title('Pareto Chart')
plt.show()
