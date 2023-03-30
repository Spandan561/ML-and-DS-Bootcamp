import seaborn as sns
import matplotlib.pyplot as plt
import pandas
df = sns.load_dataset('tips')
print(df.head())
'''''
print(df.head())
print(df.shape)
print(df.corr())
ax = sns.heatmap(df.corr())
plt.show()

#pair plot
bx = sns.pairplot(df,hue='time')
plt.show()
cx = sns.displot(df['tip'])
plt.show()
'''
sns.countplot(x='sex',data=df)
plt.show()
sns.boxplot(x='day',y='total_bill',hue='smoker',data=df)
plt.show()
sns.violinplot(x='day',y='total_bill',data=df)
plt.show()

