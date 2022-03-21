# F1 = 1
# F2 = 1
# Fn = F(n-1) + F(n-2) -->2
#
# 0 -> 0
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 6 -> 8
# 7 -> 13

results = [0,1,1]

n = 5

for i in range(2,n):
    current_result = results[-1] + results[-2]
    results.append(current_result)
    #print(current_result)

for nr in range(len(results)):
    print(f'Fib od {nr} -> {results[nr]}')