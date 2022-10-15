import matplotlib.pyplot as plt
with open('file.txt', 'r') as f:
    X, Y = zip(*[[float(s) for s in line.split()] for line in f])
plt.plot(X, Y)
plt.title('data "file.txt"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
