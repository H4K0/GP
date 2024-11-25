sl = ['Álgebra', 'Arts', 'Biology', 'Citizenship', 'Computer Science', 'Desarrollo Humano', 'English', 'Estadística', 'Filosofía', 'Física', 'Geography', 'Geometría', 'Historia', 'Lenguaje', 'Ortografía', 'Physical Education', 'Química']
superior = []
alto = []
bajo = []
superior_fin = ""
alto_fin = ""
bajo_fin = ""




#Cambiar en adelante ----->
text = input("Ingresa la notas separas por un espacio: ") ##Acá lee las notas
tbl = str.maketrans('\t', ' ')
text = text.translate(tbl)
new_text = text.replace(",",".")
nt = new_text.split(' ')

for i in range(0,17):
    nt[i] = float(nt[i])
    if nt[i] <= 2.9:
        bajo.append(sl[i])
    if nt[i] >= 3.8 and nt[i] <= 4.49:
        alto.append(sl[i])
    if nt[i] >= 4.5:
        superior.append(sl[i])

for i in range(len(bajo)):
    if i == len(bajo)-1:
        bajo_fin = bajo_fin + bajo[i] + "."
    else:
        bajo_fin = bajo_fin + bajo[i] + ", "

for i in range(len(alto)):
    if i == len(alto)-1:
        alto_fin = alto_fin + alto[i] + "."
    else:
        alto_fin = alto_fin + alto[i] + ", "

for i in range(len(superior)):
    if i == len(superior)-1:
        superior_fin = superior_fin + superior[i] + "."
    else:
        superior_fin = superior_fin + superior[i] + ", "

print("Bajo: " + bajo_fin)
print("Alto: " + alto_fin)
print("Superior: " + superior_fin)
