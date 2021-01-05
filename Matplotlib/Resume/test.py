from matplotlib import pyplot as plt

fig, ax = plt.subplots(nrows=1, ncols=1)
fig.patch.set_facecolor('xkcd:mint green')

plt.savefig('resume.png',facecolor=("xkcd:mint green"))
plt.show()

