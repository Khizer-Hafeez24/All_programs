import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fast Food', 'grilled food', 'Bar-B-Q', 'Sea Food']
Price1 = [10, 15, 20, 25]
Price2 = [25, 20, 15, 10]
Price3 = [5, 10, 15, 20]
Price4 = [20, 15, 10, 5]

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot each subplot
axs[0, 0].bar(categories, Price1)
axs[0, 0].set_title('Continental')

axs[0, 1].bar(categories, Price2)
axs[0, 1].set_title('Russian')

axs[1, 0].bar(categories, Price3)
axs[1, 0].set_title('Chinese')

axs[1, 1].bar(categories, Price4)
axs[1, 1].set_title('Pakistani')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()