import seaborn as sns
import matplotlib.pyplot as plt
df= sns.load_dataset('penguins')
df= df.dropna()

print("First 5 rows:")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print("Species:", df['species'].unique())
print("Island:", df['island'].unique())

sns.histplot(data=df, x='body_mass_g', bins=20, color='steelblue')
plt.title('Distribution of Body Mass of Penguins')
plt.xlabel('Body Mass (g)')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.title('KDE of Flipper Length by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Density')
plt.show()  

sns.histplot(data=df, x="flipper_length_mm", kde=True, color='coral')
plt.title('Flipper Length - Histogram with KDE Curve')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Count')
plt.show()

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Flipper Length vs Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

corr = df.corr(numeric_only=True)
plt.title('Correlation table:') 
print(corr)
plt.show()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Penguin Features')
plt.show()