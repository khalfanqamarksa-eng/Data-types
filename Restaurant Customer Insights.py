import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info())

sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel ('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Bill per Day by Gender (Pointplot)')
plt.xlabel ('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pairplot - Bill, Tip and Party Size', y=1.02)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Tip - Jointplot', y=1.02)
plt.show()

sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day')
plt.xlabel ('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.stripplot(x='day', y='total_bill', data=df)
plt.title('Every Bill Amount per Day (Stripplot)')
plt.xlabel ('Day')
plt.ylabel('Total Bill ($)')
plt.show()