import matplotlib.pyplot as plt
X, Y = [], []
for line in open('file.txt', 'r'):
    nilai = [float(s) for s in line.split()]
    X.append(nilai[0])
    Y.append(nilai[1])
plt.plot(X,Y)
plt.title('data "file.txt"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
          
