import pandas as pd
import os
import kagglehub
import matplotlib.pyplot as plt
import seaborn as sns

# Download latest version
path = kagglehub.dataset_download("idowuadamo/students-performance-in-2024-jamb")

print("Path to dataset files:", path)
os.listdir(path)
# read data from path using pandas
df = pd.read_csv(os.path.join(path, 'jamb_exam_results.csv'))

df.describe().T

df.tail()

df.sample(4)

df.isnull().sum()

df.info()

df[df['JAMB_Score'] == df['JAMB_Score'].max()]
df[df['JAMB_Score'] == df['JAMB_Score'].min()]

df.columns

df.shape

df.dropna(inplace=True)

df_jamb = df[['JAMB_Score']]
grp_lbl = df['Parent_Education_Level']

plt.figure(figsize=(10,8))
sns.histplot(data = df, x='JAMB_Score', hue='Parent_Education_Level') 
plt.show()

df.shape

df['Parent_Education_Level'].unique()

df.groupby('Parent_Education_Level')['JAMB_Score'].mean()
data_pel = df.groupby('Parent_Education_Level')['JAMB_Score'].mean()


plt.figure(figsize=(10,8))
sns.barplot(x=data_pel.index, y=data_pel.values)
plt.xticks(rotation=90)
plt.xlabel('Parent Education Level')
plt.ylabel('Average JAMB Score')
plt.title('Average JAMB Score by Parent Education Level')
plt.show()

grouped_data = df.groupby('Study_Hours_Per_Week')['JAMB_Score'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.regplot(x='Study_Hours_Per_Week', y='JAMB_Score', data=grouped_data)  # Use regplot for trend line
plt.title('Average JAMB Score vs. Study Hours per Week')
plt.xlabel('Study Hours per Week')
plt.ylabel('Average JAMB Score')
plt.show()
