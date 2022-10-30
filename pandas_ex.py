import pandas as pd

from matplotlib import pyplot as plt


member = pd.Series(['a', 'b', 'c'])
# print(member)

sal_1 = {'a': 130, 'b': 120, 'c': 100}
sal_2 = pd.Series(sal_1)
# print(sal_2)

plt.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = [3, 4]
y = [1, 2]

ax.bar(x, y)
plt.show()
