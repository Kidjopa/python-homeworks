m1 = len('Roman')
m2 = len('Boytsov')
m3 = len('Pavlovich')

r = int(input())

if r < min(m1, m2, m3):
    print('-42!')

else:
    for x in range(r//m1 + 1):
        for y in range(r//m2 + 1):
            for z in range(r//m3 + 1):
                if r == x*m1 + y*m2 + z*m3:
                    print(f'{x} монет m1, {y} монет m2 и {z} монет m3')
                    a = False
                    break
                else:
                    a = True
if a == True:
    print('-42!')