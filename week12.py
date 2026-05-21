import seaborn as sns

titanic = sns.load_dataset('titanic')
#print(titanic[['alive', 'survived', 'pclass', 'class', 'embarked', 'embark_town']])
titanic01 = titanic.drop(columns=['embarked', 'alive', 'class', 'deck'])
#print(titanic01.info)
#print(titanic01['deck01'])
# print(titanic01['pclass'].value_counts())
#print(titanic01[titanic01['pclass'] == 3])
# surivival_rate_pclass = titanic01.groupby('pclass')['survived'].mean()
# print(surivival_rate_pclass)
surivival_rate_sex = titanic01.groupby('sex')['survived'].mean() * 100
print(surivival_rate_sex)
