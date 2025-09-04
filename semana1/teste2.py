def mediaPonderada(nota1,nota2,nota3):
    p1 = 2
    p2 = 5
    p3 = 6
    somaP = p1+p2+p3
    mediaP = ((nota1 * p1) + (nota2 * p2) + (nota3 *p3)) /somaP
    return mediaP

notas = []
for i in range(0,3):
    nota = float(input(f"Digite sua {i+1} nota:"))
    notas.append(nota)

resultado = mediaPonderada(*notas)
print(f"Média ponderada do seu semestre = {round(resultado,2)}")
    
