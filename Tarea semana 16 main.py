#Semana 16 - TAREA
#my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Notas personales de mi semana laboral
    file.write("Nota 1: Realizar cierre tributario de Septiembre.\n")
    file.write("Nota 2: Realizar Cierre de Nomina de Personal Septiembre.\n")
    file.write("Nota 3: Citar a Asesor de Banco.\n")
    file.write("Nota 4: Mantener un equilibrio entre trabajo, entrenamiento y descanso.\n")

#Pasamos a abrir el texto con las notas
with open('my_notes.txt', 'r') as file:
    # Lectura de línea por línea
    for line in file:
        #Resultado de linea por linea
        print(line.strip())  
# utilizo strip() para eliminar espacios

# Leer la primera línea del texto de notas
with open('my_notes.txt', 'r') as file:
    first_line = file.readline() 
    print("Primera línea:", first_line.strip())
