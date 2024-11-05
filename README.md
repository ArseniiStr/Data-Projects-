# Data-Projects-


# I. Median Salary Poland
2. ![image](https://github.com/user-attachments/assets/9188a578-0d47-4494-ae9b-ffa44ff4028a)
```python
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt
import ast
import seaborn as sns

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
df_PL = df[(df['job_country'] == 'Poland')].dropna(subset=['salary_year_avg'])
job_titles = df_PL['job_title_short'].value_counts().index[0:6].tolist()
job_titles
df_PL_top6 = df_PL[df_PL['job_title_short'].isin(job_titles)]
job_order = df_PL_top6.groupby('job_title_short')['salary_year_avg'].median().sort_values(ascending=False).index
sns.boxplot(data=df_PL_top6, x='salary_year_avg', y='job_title_short', order=job_order)
sns.set_theme(style='ticks')
plt.title('Salary Distributions in the Poland')
plt.xlabel('Yearly Salary (USD)')
plt.ylabel('')
plt.xlim(0, 600000)
ticks_x = plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K')
plt.gca().xaxis.set_major_formatter(ticks_x)
plt.show()
```
# II.Top Skills for Data Roles
4. ![image](https://github.com/user-attachments/assets/0b639c82-d193-4a70-8be8-7118cf1b576d)

# III. Work Location, Degree, Insurance.
6. ![image](https://github.com/user-attachments/assets/0cad1d62-d5c4-438d-833a-801338d58e9b)
