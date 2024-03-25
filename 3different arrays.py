import matplotlib.pyplot as plt
arr = [53,100,147,167,190]
arr1 = [10,20,30,40,50]
arr2 = [45,67,65,43,21]
plt.plot(arr)
plt.plot(arr1)
plt.plot(arr2)
plt.xlabel('Overs')
plt.ylabel('scores')
plt.title('Graph of scores by Pakistani Team in 50 overs')
plt.show()