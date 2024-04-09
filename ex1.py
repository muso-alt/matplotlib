import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("wdbc.data")

print(data)

# Histogram
plt.figure(figsize=(8, 6))
plt.hist(data['Feature1'], bins=20, color='blue', alpha=0.7)
plt.xlabel('Feature 1')
plt.ylabel('Frequency')
plt.title('Histogram of Feature 1')
plt.grid(True)
plt.show()

# Scatter
plt.figure(figsize=(8, 6))
plt.scatter(data['Feature2'], data['Feature3'], color='red', alpha=0.5)
plt.xlabel('Feature 2')
plt.ylabel('Feature 3')
plt.title('Scatter Plot of Feature 2 vs Feature 3')
plt.grid(True)
plt.show()

# Line
plt.figure(figsize=(8, 6))
plt.plot(data['Feature4'], color='green')
plt.xlabel('Index')
plt.ylabel('Feature 4')
plt.title('Line Plot of Feature 4')
plt.grid(True)
plt.show()

# Bar
plt.figure(figsize=(8, 6))
plt.bar(data['Category'], data['Feature5'], color='purple')
plt.xlabel('Category')
plt.ylabel('Feature 5')
plt.title('Bar Chart of Feature 5 by Category')
plt.grid(True)
plt.show()

# Box
plt.figure(figsize=(8, 6))
plt.boxplot(data['Feature6'])
plt.xlabel('Feature 6')
plt.title('Box Plot of Feature 6')
plt.grid(True)
plt.show()

# Heatmap
plt.figure(figsize=(8, 6))
heatmap_data = data.corr()
plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(heatmap_data)), heatmap_data.columns, rotation=45)
plt.yticks(range(len(heatmap_data)), heatmap_data.columns)
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Pie
category_counts = data['Feature7'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',
        colors=['gold', 'yellowgreen', 'lightcoral'])
plt.title('Pie Chart of Feature 7')
plt.show()

# Polar
plt.figure(figsize=(8, 6))
plt.subplot(111, polar=True)
angles = [n / float(len(data)) * 2 * 3.14 for n in range(len(data))]
plt.plot(angles, data['Feature8'], marker='o')
plt.fill(angles, data['Feature8'], alpha=0.3)
plt.title('Polar Plot of Feature 8')
plt.show()
