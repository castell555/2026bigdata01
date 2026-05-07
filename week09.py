import pandas as pd

df = pd.DataFrame({'국':[1, 6, 7], '영':[2, 4, 8], '수':[3, 5, 9], '화학':[10, 3, 11]}, index=[1, 2, 3])
print(df)
print(df.iat[1, 2])
print(df.at[2, '수'])
print(df.sample(frac=0.5))
print(df.nlargest(2, '화학'))
print(df.nsmallest(2, '화학'))
print(df.tail(2))
print(df.head(2))
#df_new = df.iloc[:, [1,3]]
#df_new = df.loc[:, '영':'화학']
#df_new = df.loc[df['국']>5, ['영','화학']]