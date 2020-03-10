def students():
    a = int(input('Число учеников в классе a: '))
    b = int(input('Число учеников в классе b: '))
    c = int(input('Число учеников в классе с: '))
    if (a%2) == 0:
        d1 = int(a/2)
    elif (a%2) == 1:
        d1 = int (a/2) +1
    if (b%2) == 0:
        d2 = int(b/2)
    elif (b%2) == 1:
        d2 = int (b/2) +1
    if (c%2) == 0:
        d3 = int(c/2)
    elif (c%2) == 1:
        d3 = int (c/2) +1
    return("количество стола",d1+d2+d3)
print(students())