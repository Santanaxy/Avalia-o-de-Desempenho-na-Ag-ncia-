nome = input("DIGITE SEU NOME: ") 

nota = float(input("DIGITE SUA NOTA:"))

if nota >= 9.0 and nota <= 10.0:
    print("EXCELENTE")
if nota >= 7.0 and nota <= 8.9: 
    print("BOM")
if nota >= 5.0 and nota <= 6.9: 
    print("REGULAR")
if nota >= 3.0 and nota <= 4.9: 
    print("RUIM")
if nota >= 2.9:
    print("CRÌTICO") 
else: 
    print("NOTA INVÀLIDA") 
    
print(f"Agente {nome} sua classificação é: {nota}")