
for l in range(1,10):
    for e in range(1,10):
        if l == e:
            continue
        num = l*1001 + e*110
        den = l*11
        d = num/den
        if not d.is_integer():
            continue
        d = int(d)
        if d >= 100 and d % 10 == l:
            b = int(d/100)
            a = int(d/10)%10
            if b != a and b != l and b != e and a != l and a != e:
                print(f'{num} / {den} = {int(d)}')


