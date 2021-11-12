
import numpy as np
import matplotlib.pyplot as plt

# plt.ioff()
# for i in range(3):
#     plt.plot(np.random.rand(10))
#     plt.title("My first plot")
#     plt.show()

count = 0
n = np.ones((3,3),np.uint8)*255
print(n)
for i in range(1,10):
    for j in range(1,10):
        count = 0
        for n in range(i-1,i+2):
            for m in range(j-1,j+2):
                count += 1
        print(count)