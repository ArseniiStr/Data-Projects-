import matplotlib.pyplot as plt
import ast
import seaborn as sns
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/refs/heads/master/data/train.csv')
df.info()
df['Survived'] = df['Survived'].replace({0: 'Died', 1: 'Alive'})
plt.figure(figsize=(6,5))
sns.set_theme(style='ticks')
sns.countplot(data=df, x='Sex', hue='Survived', palette='viridis')
plt.xlabel('Comprahansion of Died Sex')
plt.ylabel('Amount of Died')
plt.legend(title='Status')
plt.show()
df['Age'] = df['Age'].apply(lambda x: int(x) if pd.notna(x) and x.is_integer() else x)
df
df_num = df[['Age', 'SibSp', 'Parch', 'Fare']]
df_cat = df[['Survived', 'Pclass', 'Sex', 'Ticket', 'Cabin', 'Embarked']]
for i in df_num:
    plt.hist(df_num[i])
    plt.title(i)
    plt.show()
print(df_num.corr())
sns.heatmap(df_num.corr())
for i in df_cat:
    sns.set_theme(style='darkgrid')
    sns.barplot(x=df_cat[i].value_counts().index, y=df_cat[i].value_counts()).set_title(i)
    plt.show()
print(pd.pivot_table(df, index = 'Survived', columns = 'Pclass', values = 'Ticket', aggfunc='count'))
print()
print(pd.pivot_table(df, index = 'Survived', columns = 'Sex', values = 'Ticket', aggfunc='count'))
print()
print(pd.pivot_table(df, index = 'Survived', columns = 'Embarked', values = 'Ticket', aggfunc='count'))
survived_by_class = pd.pivot_table(df, index='Pclass', columns='Survived', values='PassengerId', aggfunc='count', fill_value=0)


survived_by_sex = pd.pivot_table(df, index='Sex', columns='Survived', values='PassengerId', aggfunc='count', fill_value=0)

fig, ax = plt.subplots(1, 2, figsize = (14, 5))

survived_by_class.plot(kind='barh', stacked=True, color=['lightgreen', 'salmon'], ax= ax[0])
ax[0].set_title('Survival by Class')

survived_by_sex.plot(kind='barh', stacked=True, color=['lightgreen','salmon'], ax= ax[1])
ax[1].set_title('Survival by Sex')
plt.tight_layout()
plt.show()
