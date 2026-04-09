import ticket

humans = int(input("몇 명 : "))
ages = list()
age = 0
for i in range(humans):
    age = int(input("나 이 : "))
    ages.append(age)

print(f"총 요금은 {ticket.entrance_fee(ages)}원 입니다.");
#print(ages)
