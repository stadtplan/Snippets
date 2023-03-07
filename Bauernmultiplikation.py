# Bauernmultiplikation.py

list_a = []
list_b = []

def farmers_mult (a,b):
    while (a > 0):
        list_a.append(a)
        list_b.append(b)
        a = a // 2
        b = b * 2
        # Bitwise
        # a = a >> 1
        # b = b << 1
    print('list_a: ', list_a)
    print('list_b: ', list_b)

    for x in reversed(range(len(list_a))):
        if list_a[x] % 2 == 0:
            list_b.remove(list_b[x])

    print('reduced list_b: ', list_b)

    return sum(list_b)


print("Welche Zahlen sollen multipliziert werden?")
zahl1 = int(input('#1:'))
zahl2 = int(input('#2:'))

print('Summe: ', farmers_mult(zahl1, zahl2))

#Proberechnung
print("\nKontrollergebnis: ", zahl1 * zahl2)
