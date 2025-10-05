from heron import heron

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

area = heron(a, b, c)
print(f"Площадь треугольника: {area:.2f}")