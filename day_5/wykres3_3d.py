import matplotlib.pyplot as plt

xs = [0, 1, 2, 3, 4, 5]
ys = [0, 2, 4, 2, 0, -2]
zs = [0, 1, 0, 1, 0, 1]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(xs, ys, zs, color='lightblue', edgecolor='gray')

plt.show()
