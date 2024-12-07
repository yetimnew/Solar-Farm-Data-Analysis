import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = r"D:\10x\data\week_0\projcet_one\src\benin-malanville.csv" 
data = pd.read_csv(file_path)

# Display the first few rows
# print(data.head())
# Dataset overview
# print(data.info())
# print(data.isnull().sum())

# print(data.duplicated().sum())

# Distribution of GHI
sns.histplot(data['GHI'], bins=30, kde=True)
plt.title('Distribution of Global Horizontal Irradiance (GHI)')
plt.show()