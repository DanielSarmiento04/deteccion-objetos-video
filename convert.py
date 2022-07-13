# Open requeriments.txt
f = open('requirements.txt', 'r')
f2 = open('newRequeriment.txt', 'w')
for linea in f:
    # Split linea in words
    if linea[0] != ' ':
        newLinea = linea.split("==")
        f2.write(newLinea[0]+"\n")
        
f2.close()
    # print(linea)