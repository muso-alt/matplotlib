import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Подключение к репозиторию и загрузка данных
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=column_names)

# Построение графиков Seaborn
sns.set(style="whitegrid")

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_length'], kde=True, color='blue')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='class')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# Line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df.drop(columns='class'))
plt.title('Line Plot')
plt.show()

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='class', y='sepal_length', data=df)
plt.title('Bar Plot of Sepal Length by Class')
plt.xlabel('Class')
plt.ylabel('Sepal Length')
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='class', y='sepal_length', data=df)
plt.title('Box Plot of Sepal Length by Class')
plt.xlabel('Class')
plt.ylabel('Sepal Length')
plt.show()

# Heatmap
numeric_df = df.drop(columns=['class'])
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Pie chart
plt.figure(figsize=(10, 6))
df['class'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Pie Chart of Class Distribution')
plt.ylabel('')
plt.show()

# Построение графиков Plotly
# 3D Scatter plot
fig = go.Figure(data=go.Scatter3d(
    x=df['sepal_length'],
    y=df['sepal_width'],
    z=df['petal_length'],
    mode='markers',
    marker=dict(
        size=8,
        color=df['class'].astype('category').cat.codes,
        colorscale='viridis',
        opacity=0.8
    )
))

fig.update_layout(
    scene=dict(
        xaxis=dict(title='Sepal Length'),
        yaxis=dict(title='Sepal Width'),
        zaxis=dict(title='Petal Length')
    ),
    margin=dict(r=0, l=0, b=0, t=0),
    title="3D Scatter Plot of Sepal Length, Sepal Width, and Petal Length"
)

fig.show()
