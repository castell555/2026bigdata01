import seaborn as sns
# import matplotlib.pyplot as plt

#(데이터 측정)년도, (대상)국가, (1인당 연간 의료비)지출액, (평균)기대수명
health = sns.load_dataset("healthexp")
# 가장 최근 연도인 2020년 데이터를 필터링 후 추출
# health_2020 = health[health['Year']==2020]
# print(health_2020)
# print(health_2020.sort_values(by=['Life_Expectancy'], ascending=False))
# print(health_2020.sort_values(ascending=False, 'Life_Expectancy'))