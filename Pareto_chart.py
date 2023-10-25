import matplotlib.pyplot as plt

# Sample data (replace with your own)
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
frequency = [10, 8, 6, 4, 2]

# Calculate cumulative frequency
cumulative_frequency = [sum(frequency[:i+1]) for i in range(len(frequency))]

# Create the Pareto chart
fig, ax1 = plt.subplots()

# Create the bar chart
ax1.bar(categories, frequency, color='b')
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
