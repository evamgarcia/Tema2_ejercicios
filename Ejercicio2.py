#Transforma este texto:
#un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro #monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
#En este otro:
#Un día que el viento soplaba con fuerza...
#- Mira como se mueve aquella banderola -dijo un monje.
#- Lo que se mueve es el viento -respondió otro monje.
#- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
#Lo único prohibido es modificar directamente el texto.

texto = 'un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro'
linea_linea = texto.split('#')
for elemento, linea in enumerate(linea_linea):
    linea_linea[elemento] = linea.capitalize()
    if elemento == 0:
        linea_linea[elemento] = linea_linea[elemento] + "..."
    else:
        linea_linea[elemento] = "- " + linea_linea[elemento] + "."
for linea in linea_linea:
    print(linea)