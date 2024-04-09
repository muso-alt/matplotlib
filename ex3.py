import pandas as pd
import ipywidgets as widgets
from IPython.display import display
from matplotlib import pyplot as plt

# Загрузка набора данных
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=column_names)

# Создание выпадающего списка с названиями колонок DataFrame
dropdown = widgets.Dropdown(options=df.columns, description='Column:')

# Функция для создания графика по выбранной колонке
def create_plot(column):
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Обработчик события для кнопки
def on_button_clicked(b):
    column = dropdown.value
    create_plot(column)

# Создание кнопки
button = widgets.Button(description="Create Plot")

# Подключение обработчика события к кнопке
button.on_click(on_button_clicked)

# Отображение интерфейса
display(widgets.Label(value="Select a column to plot:"))
display(dropdown)
display(button)
