import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file
data = pd.read_csv('/content/Student Numbers 2nd file.csv')
print(data.head())

# Set maximum rows to display
pd.options.display.max_rows = 70

# Line plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(data['Maths'], data['Science'], marker='o', linestyle='-')
plt.title('Maths vs Science')
plt.xlabel('Maths')
plt.ylabel('Science')

# Scatter plot
plt.subplot(1, 2, 2)
plt.scatter(data['Maths'], data['Science'])
plt.title('Maths vs Science (Scatter)')
plt.xlabel('Maths')
plt.ylabel('Science')

# Pie chart
plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.pie(data['Maths'], labels=data['Science'], autopct='%1.1f%%')
plt.title('Maths Distribution')

plt.show()
#simple graph
plt.plot(data['Maths'], data['Science'])  # 'Science' should be within quotes
plt.show()