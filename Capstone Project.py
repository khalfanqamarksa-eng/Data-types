import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())
df= sns.load_dataset('penguins')
print(df.head(10))
print(df.shape)
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.info())
print(df.describe(include='all'))
print(df.corr(numeric_only=True))
sns.heatmap(df.corr(numeric_only=True), annot=True,)
plt.show()
df.select_dtypes(include=[np.number]).hist(figsize=(49, 57))
plt.show()
df.select_dtypes(include=['number']).plot(kind='box', subplots=True, layout=(3, 2), sharex=False, sharey=False, figsize=(12, 8))
plt.show()

print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())

sns.pointplot(data=df, x='sex', y='body_mass_g')
plt.show()

sns.jointplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.show()

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.show()

sns.swarmplot(data=df, x='species', y='bill_length_mm', hue='sex')
plt.show()

sns.lmplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='sex')
plt.show()

sns.boxplot(data=df, x='species', y='body_mass_g', hue='sex')
plt.show()

sns.pairplot(data=df, hue="species")
plt.show()