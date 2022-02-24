print('Dzień dobry, podaj proszę aktualną cenę benzyny za 1 litr:')
fuel_cost=float(input())
print('Cena 1 litra benzyny:',fuel_cost,'zł')
print('Podaj proszę szacowany dystans w kilometrach')
distans=float(input())
print('Dystans do pokonania',distans,"km")
print('Podaj proszę spalanie ilości paliwa przez twoje auto na 100km (w litrach):')
burn=(float(input()))/100
print('Spalania auta',burn*100,"l/100km")
fuel=burn*distans
cost=fuel_cost*fuel
print('Koszt podróży w jedną stronę wyniesie',round(cost,2),'zł')