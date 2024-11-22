import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import ast as ast
df = pd.read_csv('C:/Users/VXd/Downloads/employee_evaluation_dataset.csv')
df
# Идеи для анализа: 
# 1. Общее кол-во, оценок.
# 2. Средняя оценка по всем критериям и по отдельности.
# 3. В каком критерии худшая оценка, а в каком лучшая. (средне)
# 4. Графики через fig, ax для всего. 


categories = ['Salary', 'Work Conditions', 'Atmosphere', 'Management Attitude', 'Potential', 'Career Growth']
df['Average Score'] = df[categories].mean(axis=1).round(1) # Добавляем среднюю оценку для каждого сотрудника
# Преобразуем строку суммы в DataFrame и добавляем к основному DataFrame
# Исключаем строку Total для расчёта среднего
# Рассчитываем средние значения по категориям и округляем до одного знака
average_category = df[categories].mean().round(decimals=1)

average_all = df[categories].mean(axis=0).round(decimals=1)
average_category_row = pd.DataFrame([average_all], columns=df.columns)
average_category_row['Employee_ID'] = 'Average Category'
average_category_row['Average Score'] = np.nan

df = pd.concat([df, average_category_row], ignore_index=True)
df['Employee_ID'].drop_duplicates(keep='first')
df
average_all.plot(kind='barh', stacked=True)
from matplotlib.ticker import PercentFormatter
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}'))
df
from matplotlib.ticker import PercentFormatter
df_filtered = df[df['Employee_ID'] != 'Average Category']
for i in categories:
    plt.figure()
    value_counts = df_filtered[i].value_counts().reindex(range(1, 6), fill_value=0).sort_index()
    sns.barplot(x=value_counts.index, y=value_counts.values, color='skyblue').set_title(i)
    plt.show()
    import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import pandas as pd

# Создадим DataFrame со значениями оценок и категорий для удобства построения общего графика
df_melted = pd.melt(df[categories], value_vars=categories, var_name='Категория', value_name='Оценка')

# Построим график
g = sns.FacetGrid(df_melted, col='Категория', col_wrap=3, height=5, sharey=True)  # col_wrap=3 - по три графика в строке
g.map_dataframe(sns.histplot, x='Оценка', color='skyblue', discrete=True, shrink=0.8)

# Форматирование оси Y для отображения целых значений
for ax in g.axes.flat:
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

g.set_axis_labels("Оценка", "Количество")  # Устанавливаем общие названия осей
g.set_titles("{col_name}")  # Устанавливаем названия категорий как заголовки для каждого графика

plt.tight_layout()  # Чтобы графики не перекрывали друг друга
plt.show()