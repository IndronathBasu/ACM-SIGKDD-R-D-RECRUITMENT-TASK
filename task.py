import pandas as pd

# Loading Data
df = pd.read_csv(r"tested.csv")

# Data Inspection
print(df.head())
print(df.info())
print(df.describe())

# Data Selection
s_c = df[['Age', 'Pclass', 'Survived']]
print(s_c.head())

# Filtering
s_p = df[df['Survived'] == 1]
print(s_p.head())

# Handling Missing Data
print(df.isnull().sum())  # Checking missing values
df_cleaned = df.dropna()  # Removing rows with missing values
df['Age'] = df['Age'].fillna(df['Age'].median())  # Filling missing Age with median
print(df.isnull().sum())  # Verifying missing values after handling
