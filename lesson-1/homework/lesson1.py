s = int(input("enter the length of the square:4 "))
perimeter = 4 * s
area = s ** 2
print(f"Kvadratning perimetri: {perimeter}")
print(f"Kvadratning yuzasi: {area}")

d = float(input("Doiraning diametrini kiriting (d):4 "))
length = math.pi * d
print(f"Doiraning uzunligi: {length}")

a = float(input("Birinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))
mean = (a + b) / 2
print(f"Ikkala sonning o'rtachasi: {mean}")

a = float(input("Birinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))

sum_ab = a + b
product = a * b
square_a = a ** 2
square_b = b ** 2

print(f"Yig'indisi: {sum_ab}")
print(f"Ko'paytmasi: {product}")
print(f"a ning kvadrati: {square_a}")
print(f"b ning kvadrati: {square_b}")
