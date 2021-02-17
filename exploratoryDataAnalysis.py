import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from scipy import stats

path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
display(df.head())

#displaying datatypes, and calculating correlation coefficients across all attributes
display(df.dtypes)
df.corr()

#calculate and show correlation coefficients between the following attributes
print(df[['bore','stroke','compression-ratio','horsepower']].corr())

#scatterplot of engine size and price
'''sns.regplot(x='engine-size', y='price', data=df)
plt.ylim(0,)
print(df[['engine-size','price']].corr())'''

#scatterplot of highway mpg and price
'''sns.regplot(x='highway-mpg', y='price', data=df)
print(df[['highway-mpg','price']].corr())'''

#scatterplot of peak rpm and price
'''sns.regplot(x='peak-rpm', y='price', data=df)
print(df[['peak-rpm','price']].corr())'''

#scatterplot of stroke and price
'''sns.regplot(x='stroke', y='price', data=df)
print(df[['stroke','price']].corr())'''

#boxplot of body style and price
'''sns.boxplot(x='body-style', y='price', data=df)
print(df[['body-style', 'price']].corr())'''

#boxplot of drive wheels and price
'''sns.boxplot(x='drive-wheels', y='price', data=df)
print(df[['drive-wheels','price']].corr())'''


#describe the dataframe
display(df.describe())

#computing value counts for column drive wheels and creating a dataframe
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
display(drive_wheels_counts)
drive_wheels_counts.index.name = 'drive-wheels'
display(drive_wheels_counts)

# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
display(engine_loc_counts.head(10))

#finding unique objects in drive wheels column
print(df['drive-wheels'].unique())

#grouping drive wheels, body style, and price into a new dataframe
df_group_one = df[['drive-wheels', 'body-style', 'price']]
display(df_group_one)
df_group_one = df_group_one.groupby(['drive-wheels'], as_index=False).mean()
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
display(grouped_test1)

#creating a pivot table
grouped_pivot = grouped_test1.pivot(index='drive-wheels', columns='body-style')
grouped_pivot = grouped_pivot.fillna(0)
display(grouped_pivot)

#grouping by body style and price, to find the mean price for each body style
df_group_two = df[['drive-wheels', 'body-style', 'price']]
df_group_two = df_group_two.groupby(['body-style'], as_index=False).mean()
display(df_group_two)

#plotting grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

plt.xticks(rotation=90)
fig.colorbar(im)
plt.show()

#calculating p values

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

grouped_test2 = df_gptest[['drive-wheels','price']].groupby(['drive-wheels'])
display(grouped_test2.get_group('4wd')['price'])

# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val) 












