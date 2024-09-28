import pandas as pd

data1 = pd.read_csv('C:/Users/desir/Downloads/Sepal_Data.csv')
data2 = pd.read_csv('C:/Users/desir/Downloads/Petal_Data.csv')

data = pd.concat([data1, data2], ignore_index=True)

print(data.dtypes)  
print(data.head())  

for column in data.columns:
    if data[column].dtype == 'object': 
        data[column] = pd.to_numeric(data[column], errors='coerce')

print(data.isnull().sum())

correlation_matrix = data.corr()
print("Correlation Matrix:")
print(correlation_matrix)

averages = data.mean()
print("\nAverages of each variable:")
print(averages)

medians = data.median()
print("\nMedians of each variable:")
print(medians)

standard_deviations = data.std()
print("\nStandard Deviations of each variable:")
print(standard_deviations)

print("\nSpecies comparison based on correlation of measurements:")
species_comparison = data.groupby('species').corr()
print(species_comparison)