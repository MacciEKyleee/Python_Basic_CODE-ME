day=24
hour=60
week=7
hw=7
print(day*hour*week*hw)

# Ilość godzin nauki
knl=75

# Ilość godzin nauki dziennie
#hpd=2
print("Podaj ile godzin dziennie chcesz się uczyć")
hpd = int(input())

print("Dziennie (łącznie z sobotami i niedzielami, będę uczył się",hpd,"godziny")
days=(knl//hpd)+1

weeks=(days//7)+1
print("Nauka zajmie mi ", str(weeks),"pełnych tygodni")

weeks_without=(days//5)+1
print("Nauka zajmie mi ", str(weeks_without),"tygodni roboczych")
