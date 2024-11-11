# Data-Projects-


## I. Median Salary Poland
<img src="https://github.com/user-attachments/assets/9188a578-0d47-4494-ae9b-ffa44ff4028a" width = "700px" /> 
<details>
  <summary>Click to expand Python code</summary>
    
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
</details>

### 📊 Insights

This project focuses on analyzing salary distributions for various job titles in 🇵🇱 Poland using data from the `lukebarousse/data_jobs` dataset. By leveraging Python 🐍 and key libraries like `pandas` 🐼, `seaborn` 📈, and `matplotlib` 📊, the analysis highlights differences in compensation across six popular job titles within the dataset.

#### 🔍 Key Steps in the Analysis
- **Data Cleaning and Transformation**: Converted job posting dates to a consistent datetime format 📅 and processed skill data. Filtered the dataset to include only entries with valid salary data for Poland.
- **Top Job Titles Identification**: Identified the six most common job titles to focus the salary analysis on the most relevant roles in the dataset.
- **Salary Distribution Analysis**: Visualized the yearly salary distribution for each top job title with a box plot 📦, ordered by median salary for easy comparison.

#### 📈 Visual Insights
The final plot clearly displays the range and distribution of yearly salaries for different job titles, helping to identify roles with higher median salaries and understand the overall salary variability. This provides a quick reference for individuals interested in job market trends and salary expectations for specific roles in Poland.

#### 🛠️ Tools Used
- `pandas` 🐼 for data manipulation and cleaning
- `ast` 🧩 for parsing complex skill data
- `seaborn` 📈 and `matplotlib` 📊 for data visualization and custom plot styling


## II. 📈 Top Skills for Data Roles
<img src="https://github.com/user-attachments/assets/0b639c82-d193-4a70-8be8-7118cf1b576d" width="700px" />

This section analyzes the top skills required for data roles in the 🇺🇸 United States using the `lukebarousse/data_jobs` dataset. By leveraging Python 🐍 libraries like `pandas` 🐼 and `seaborn` 📈, we extracted the top three job titles and identified the five most frequently mentioned skills for each role. This allows us to understand the key competencies valued in the U.S. data job market.

### 🔍 Key Steps in the Analysis
- **Data Filtering**: Filtered the dataset for U.S.-based job postings and exploded skill lists to make skill counting easier.
- **Top Job Titles**: Selected the top three job titles based on frequency in the dataset.
- **Top Skills Analysis**: For each title, identified the five most in-demand skills using grouped counts and displayed these in horizontal bar charts for easy comparison.

### 📊 Visual Insights
Each subplot in the figure highlights the skill count for one of the top job titles, showing the most in-demand skills by job type. This gives a clear overview of the technical requirements specific to each role.

### 🛠️ Tools Used
- `pandas` 🐼 for data manipulation and transformation
- `ast` 🧩 for parsing skill data from strings to lists
- `seaborn` 📈 and `matplotlib` 📊 for data visualization and custom plot styling

<details>
  <summary>Click to expand Python code</summary>

  ```python
  import pandas as pd 
  from datasets import load_dataset
  import matplotlib.pyplot as plt
  import ast
  import seaborn as sns

  # Load dataset
  dataset = load_dataset('lukebarousse/data_jobs')
  df = dataset['train'].to_pandas()

  # Data processing
  df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
  df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
  df_US = df[df['job_country'] == 'United States']
  df_skills = df_US.explode('job_skills')

  # Count skills by job title
  df_skills_count = df_skills.groupby(['job_skills', 'job_title_short']).size()
  df_skills_count = df_skills_count.reset_index(name='skill_count')
  df_skills_count.sort_values(by='skill_count', ascending=False, inplace=True)

  # Select top 3 job titles
  job_titles = df_skills_count['job_title_short'].unique().tolist()
  job_titles = sorted(job_titles[:3])

  # Plot top 5 skills for each job title
  fig, ax = plt.subplots(len(job_titles), 1, figsize=(8, 10))
  for i, job_title in enumerate(job_titles):
      df_plot = df_skills_count[df_skills_count['job_title_short'] == job_title].head(5)
      df_plot.plot(kind='barh', x='job_skills', y='skill_count', ax=ax[i], title=job_title)
      ax[i].invert_yaxis()
      ax[i].set_ylabel('')
      ax[i].legend().set_visible(False)
  fig.suptitle('Counts of Top Skills in Job Postings', fontsize=15)
  plt.tight_layout(h_pad=0.5)
  plt.show()
```
</details>


## III. 🌍 Work Location, 🎓 Degree Requirement, and 🏥 Health Insurance

This section provides insights into job locations, degree requirements, and health insurance offerings for Data Analyst roles in the 🇺🇸 United States. Using the `lukebarousse/data_jobs` dataset, we analyzed the top job locations, the mention of degree requirements, and the availability of health insurance benefits.

### 🔍 Key Insights
- **Top Locations**: The bar chart shows the top 10 U.S. cities with the highest number of job postings for Data Analysts.
- **Degree and Benefits**: The pie charts display the distribution of jobs based on:
  - **Work-from-home opportunities** 🏠
  - **Degree requirements** 🎓
  - **Health insurance offerings** 🏥

### 🛠️ Tools Used
- `pandas` 🐼 for data manipulation
- `matplotlib` 📊 and `seaborn` 📈 for data visualization

<img src="https://github.com/user-attachments/assets/0cad1d62-d5c4-438d-833a-801338d58e9b" width="700px" />

<details>
  <summary>Click to expand Python code</summary>

  ```python
  import pandas as pd 
  from datasets import load_dataset
  import matplotlib.pyplot as plt
  import ast
  import seaborn as sns

  # Load dataset
  dataset = load_dataset('lukebarousse/data_jobs')
  df = dataset['train'].to_pandas()

  # Preprocess data
  df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
  df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

  # Filter for US Data Analyst roles
  df_DA_US = df[(df['job_country'] == 'United States') & (df['job_title_short'] == 'Data Analyst')]
  
  # Top 10 job locations
  df_plot = df_DA_US['job_location'].value_counts().head(10).to_frame()
  sns.set_theme(style='ticks')
  sns.barplot(data=df_plot, x='count', y='job_location', palette='dark:b_r', legend=False)
  sns.despine()
  plt.title('Counts of Job Locations for Data Analyst in the US')
  plt.xlabel('Number of Jobs')
  plt.ylabel('')
  plt.show()

  # Degree and insurance distribution
  dict_column = {
      'job_work_from_home': 'Work From Home',
      'job_no_degree_mention': 'Job Degree Req.',
      'job_health_insurance': 'Health Insurance Offered'
  }
  fig, ax = plt.subplots(1, 3, figsize=(12, 5))
  for i, (column, title) in enumerate(dict_column.items()):
      ax[i].pie(df_DA_US[column].value_counts(), startangle=90, autopct='%1.1f%%', labels=['False', 'True'])
      ax[i].set_title(title)
  fig.tight_layout()
  plt.show()
```
</details>
## IV. 💼 Salary Vs. Count of Job Postings for Top 10 Skills

This section highlights the relationship between the **frequency** of specific skills in job postings and the **median salary** offered for those skills. The plot helps identify which skills are in high demand and how they correlate with compensation levels.

### 🔍 Key Insights
- **Top Skills**: The scatter plot shows the top 10 most demanded skills for Data Analysts and their corresponding median yearly salaries in USD.
- **Salary Correlation**: Skills that appear more frequently in job postings do not necessarily guarantee higher salaries, offering insight into supply-demand dynamics for data skills.

### 🛠️ Tools Used
- `pandas` 🐼 for data manipulation
- `matplotlib` 📊 for visualization
- `adjustText` 📌 for label adjustments

<img src="https://github.com/user-attachments/assets/dad78519-c1a1-42c5-a8f5-f3a3760f4dd2" width="700px" />

<details>
  <summary>Click to expand Python code</summary>

  ```python
  import pandas as pd 
  from datasets import load_dataset
  import matplotlib.pyplot as plt
  import ast
  from adjustText import adjust_text

  # Load and prepare dataset
  dataset = load_dataset('lukebarousse/data_jobs')
  df = dataset['train'].to_pandas()

  df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
  df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

  # Filter and explode data
  df = df[df['job_title_short'] == 'Data Analyst']
  df_exploded = df.explode('job_skills')

  # Group by skill and calculate statistics
  skill_stats = df_exploded.groupby('job_skills').agg(
      skill_count=('job_skills', 'count'),
      median_salary=('salary_year_avg', 'median')
  )
  skill_count = 10
  skill_stats = skill_stats.sort_values(by='skill_count', ascending=False).head(skill_count)

  # Plotting
  skill_stats.plot(kind='scatter', x='skill_count', y='median_salary')
  texts = []
  for i, txt in enumerate(skill_stats.index):
      texts.append(plt.text(skill_stats['skill_count'].iloc[i], skill_stats['median_salary'].iloc[i], txt))

  # Adjust text labels for clarity
  adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))
  ax = plt.gca()
  ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K'))
  plt.xlabel('Count of Job Postings')
  plt.ylabel('Median Yearly Salary ($USD)')
  plt.title('Salary vs. Count of Job Postings for Top 10 Skills')
  plt.tight_layout()
  plt.show()
```
</details>




## 🚢 Titanic Data Analysis: Survival Insights by Class and Sex

This analysis provides insights into the survival distribution by class and sex on the Titanic. Through visualizations, we can observe how different demographics were affected by survival outcomes.

### 🔍 Key Insights
- **Class and Survival**: Passengers in higher classes had different survival rates compared to those in lower classes, showcasing potential socio-economic impacts on survival.
- **Gender and Survival**: The data reflects significant differences in survival rates between male and female passengers.

### 🛠️ Tools Used
- `pandas` 🐼 for data manipulation
- `matplotlib` 📊 and `seaborn` for visualizations

---


### 1. Passenger Demographics and Survival Distribution
This section shows the distribution of survivors across genders.

<details>
  <summary>Click to view Python code</summary>

  ```python
  import matplotlib.pyplot as plt
  import seaborn as sns
  import pandas as pd

  # Load data
  df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/refs/heads/master/data/train.csv')
  df['Survived'] = df['Survived'].replace({0: 'Died', 1: 'Alive'})

  # Survival by Gender Plot
  plt.figure(figsize=(6,5))
  sns.set_theme(style='ticks')
  sns.countplot(data=df, x='Sex', hue='Survived', palette='viridis')
  plt.xlabel('Comparison of Gender')
  plt.ylabel('Number of Passengers')
  plt.legend(title='Survival Status')
  plt.show()

# Numerical and Categorical Data Preparation
df['Age'] = df['Age'].apply(lambda x: int(x) if pd.notna(x) and x.is_integer() else x)
df_num = df[['Age', 'SibSp', 'Parch', 'Fare']]
df_cat = df[['Survived', 'Pclass', 'Sex', 'Ticket', 'Cabin', 'Embarked']]

# Histograms for Numerical Data
for i in df_num:
    plt.hist(df_num[i].dropna(), bins=10, color='skyblue')
    plt.title(i)
    plt.show()

# Correlation Heatmap
sns.heatmap(df_num.corr(), annot=True, cmap="coolwarm")
plt.show()

# Barplots for Categorical Data
for i in df_cat:
    sns.barplot(x=df_cat[i].value_counts().index, y=df_cat[i].value_counts(), palette='viridis')
    plt.title(i)
    plt.show()
# Survival Analysis by Class and Sex
survived_by_class = pd.pivot_table(df, index='Pclass', columns='Survived', values='PassengerId', aggfunc='count', fill_value=0)
survived_by_sex = pd.pivot_table(df, index='Sex', columns='Survived', values='PassengerId', aggfunc='count', fill_value=0)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Survival by Class
survived_by_class.plot(kind='barh', stacked=True, color=['lightgreen', 'salmon'], ax=ax[0])
ax[0].set_title('Survival by Class')

# Survival by Sex
survived_by_sex.plot(kind='barh', stacked=True, color=['lightgreen', 'salmon'], ax=ax[1])
ax[1].set_title('Survival by Sex')

plt.tight_layout()
plt.show()
```
</details>

<img src="https://github.com/user-attachments/assets/2b8fb73c-acae-48e4-9e1b-c647f892e300" width="350px" />
<img src="https://github.com/user-attachments/assets/16c34386-b289-48c8-8f9b-a264070dd1c7" width="350px" />
<img src="https://github.com/user-attachments/assets/474d57e4-c73e-4a58-98f5-f039f4ddd598" width="350px" />
<img src="https://github.com/user-attachments/assets/108c1793-c356-432c-801c-97ac1af0e993" width="350px" />











