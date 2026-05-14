import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg['model_year'].value_counts().sort_values(ascending=False))
print(mpg.sort_values('model_year',ascending=False))