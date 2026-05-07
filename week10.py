import seaborn as sns

mpg = sns.load_dataset('mpg')
mpg = mpg.drop(columns=['origin', 'model_year', 'name'])
#print(mpg.sort_values('mpg', ascending=False))
# print(mpg.info())
# print(mpg.describe())
# print(mpg['cylinders'].value_counts())
# print(mpg[mpg['horsepower'].isnull()])
# mpg['horsepower'] = mpg['horsepower'].fillna(
#     mpg.groupby('cylinders')['horsepower'].transform('median')
# )
# print(mpg.info())
# print(mpg[mpg['horsepower'].isnull()])