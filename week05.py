#import ticket

humans = int(input("몇 명 : "))
ages = list()
age = 0
for i in range(humans):
    age = int(input("나 이 : "))
    ages.append(age)

print(ages)