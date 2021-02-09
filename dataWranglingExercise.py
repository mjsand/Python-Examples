import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
from IPython.display import display
import numpy as np

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
 
df = pd.read_csv(filename, names=headers)

#convert missing values from '?' to NaN

df.replace("?", np.nan, inplace = True)
display(df.head())

#display missing values as boolean
missing_data = df.isnull()
display(missing_data.head())

# counter number of columns with missing data
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
    
#calculate average of normalized-losses
avg_norm_loss = df["normalized-losses"].astype('float').mean(axis=0)
print('Average of normalized-losses:', avg_norm_loss)

#replacing 'NaN' values in normalized-losses with mean value
df['normalized-losses'].replace(np.nan, avg_norm_loss, inplace=True)

# calculate mean value for bore column
avg_bore = df['bore'].astype('float').mean(axis=0)
print('Average bore:', avg_bore)

#replacing bore 'NaN' values with mean value for column
df['bore'].replace(np.nan, avg_bore, inplace=True)

#calculate mean for Stroke and replace NaN values with it
avg_stroke = df['stroke'].astype('float').mean(axis=0)
print('Average stroke:', avg_stroke)
df['stroke'].replace(np.nan, avg_stroke, inplace=True)

#calculate average horsepower and replace NaN values with it
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

#calculate mean for peak-rpm and replace NaN values with it
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

#calculate most common (mode) door configuration for vehicles
df['num-of-doors'].value_counts()
print(df['num-of-doors'].value_counts().idxmax())

#replacing NaN values in num-of-doors with mode value
df['num-of-doors'].replace(np.nan, 'four', inplace=True)

#dropping whole row with NaN in price column
df.dropna(subset=['price'], axis=0, inplace=True)

#reset index, because we dropped two rows
df.reset_index(drop=True, inplace=True)

#displaying new dataframe with corrected values
display(df.head())

#displaying current data types in each column
print(df.dtypes)

#correcting data types for each column
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses", 'horsepower']] = df[["normalized-losses", 'horsepower']].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

#check data types again after correction
print(df.dtypes)

#convert mpg to L/100km
df['city-L/100km'] = 235/df['city-mpg']
display(df.head())

df['highway-L/100km'] = 235/df['highway-mpg']
display(df.head())

# replace (original value) by (original value)/(maximum value) to normalize data
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()

#binning horsepower data
df['horsepower'] = df['horsepower'].astype(int, copy=True)

#plotting histogram of horsepower
'''plt.pyplot.hist(df['horsepower'])
plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')'''

#building a bin
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
df[['horsepower', 'horsepower-binned']].head(20)
df['horsepower-binned'].value_counts()
pyplot.bar(group_names, df['horsepower-binned'].value_counts())
plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')


#creating dummy variables
dummy_variable_1 = pd.get_dummies(df['fuel-type'])
dummy_variable_1.head()
dummy_variable_1.rename(columns={'gas': 'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)


#merge data frame 'df' and 'dummy_variable_1'
df = pd.concat([df, dummy_variable_1], axis=1)
df.drop('fuel-type', axis=1, inplace=True)

#creating dummy variable for aspiration type
dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.rename(columns={'std': 'aspiration-std', 'turbo':'aspiration-turbo'}, inplace=True)
display(dummy_variable_2.head())

#merge data from dummy_variable_2 with df
df = pd.concat([df, dummy_variable_2], axis=1)
df.drop('aspiration', axis=1, inplace=True)

#save df to new csv file
df.to_csv('clean_df.csv')

















