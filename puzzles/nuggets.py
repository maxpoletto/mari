m = [ 1 ] * 101
m[0] = 0

for i in range(0, 17): # 17 * 6 = 102
    for j in range(0, 12): # 12 * 9 = 108
        for k in range(0, 6): # 6 * 20 = 120
            p = 6 * i + 9 * j + 20 * k
            if p <= 100:
                m[p] = 0
print(m)
c = sum(m)
print("La probabilité que la commande ne puisse pas être satisfaite est de", c, "%")
