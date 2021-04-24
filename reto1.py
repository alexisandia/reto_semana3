
lista_notas=[]
i=0
#almacenar las 5 notas
while i<5:
#insertar nota
    nota = input(f"Ingrese nota{i+1}: ")
#deteccion de error y agregar a la lista
    try:
        nota = int(nota)
        lista_notas.append(nota)
        i=i+1
    except (TypeError, ValueError) as e:
        print(f'El valor ingresado no es un número')

#obtener mayor, menor y promedio
print(f'Nota mayor: {max(lista_notas)}')
print(f'Nota menor: {min(lista_notas)}')
print(f'Promedio de notas: {(sum(lista_notas)/int(len(lista_notas)))}\n')
