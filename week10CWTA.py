import matplotlib.pyplot as plt

x = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
y = [6,8,5,6,5,10,10]

plt.xlabel("Days")
plt.ylabel("Hours of Sleep")
plt.plot(x,y)
plt.grid(True)

plt.show()
