import matplotlib.pyplot as plt
from Series.read_csv import subs,s
subs.plot()
plt.show()
s.value_counts().head(20).plot(kind='bar')
s.plot()
plt.show()