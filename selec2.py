Lista = [4, 2, 6, 8, 5, 7, 0]

for i in range(1, len(Lista)):
    aux = Lista[i]
    j = i - 1

    while j >= 0 and aux < Lista[j]:
        Lista[j + 1] = Lista[j]
        Lista[j] = aux
        j -= 1

print(Lista)