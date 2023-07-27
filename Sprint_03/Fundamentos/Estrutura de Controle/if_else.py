nota = float(input("Nota: "))

if nota > 10:
    print("Sua nota foi: A")
elif  nota >= 8.1:
    print("Sua nota foi: A-")
elif  nota >= 7.1:
    print("Sua nota foi: B")
elif  nota >= 6.1:
    print("Sua nota foi: B-")
elif  nota >= 5.1:
    print("Sua nota foi: C")
elif  nota >= 4.1:
    print("Sua nota foi: C-")
elif nota >= 3.1:
    print("Sua nota foi: D")
elif  nota >= 2.1:
    print("Sua nota foi: D-")
elif  nota >= 1.1:
    print("Sua nota foi: E")
elif  nota >= 0.0:
    print("Sua nota foi: E-")
else:
    print("Nova inválida")