import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info)

#Barplot
sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel ('Day')
plt.ylabel('Average Bill ($)')
plt.show()

#Countplot
sns.countplot(x='day', hue='sex', data=df)
plt.title('Count of Diners per Day by Gender')
plt.xlabel ('Day')
plt.ylabel('Count')
plt.show()

#Boxplot
sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day')
plt.xlabel ('Day')
plt.ylabel('Total Bill ($)')
plt.show()

#Stripplot
sns.stripplot(x='day', y='total_bill', data=df)
plt.title('Every Bill Amount per Day (Stripplot)')
plt.xlabel ('Day')
plt.ylabel('Total Bill ($)')
plt.show()

#Swarmplot
sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Every Bill Amount per Day (Swarmplot)')
plt.xlabel ('Day')
plt.ylabel('Total Bill ($)')
plt.show()

#Pairplot
sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pairplot - Bill, Tip and Party Size', y=1.02)
plt.show()

#Pointplot
sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Bill per Day by Gender (Pointplot)')
plt.xlabel ('Day')
plt.ylabel('Average Bill ($)')
plt.show()

#Implot
sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Tip - Trend Line')
plt.show()