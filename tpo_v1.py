def añadiralista(lista,elemento):
    #añade elementos a una lista
    lista.append(elemento)
    return lista

def winrate(elemento):
        #devuelve una lista con el pais sus victorias, partidos, porcentaje de cunatos partidos gano
        p = (local.count(elemento))+(visita.count(elemento))
        lv = localganadores.count(elemento)
        vv = visitaganadores.count(elemento)
        r = [elemento,vv+lv,p,lv,vv,(vv+lv)*100/p]
        return r

def imprimirmatriz(matriz):
     # Imprimir la matriz
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")  # Imprimir cada elemento de la fila separado por espacio
        print()  # Saltar a una nueva línea después de imprimir cada fila   

try:
    #Apertura del archivo
    file = open(r'C:\Users\buizf\OneDrive\Escritorio\tpo programacion 1\EJERCICIO SOBRE EL ARCHIVO\penality kick.csv.csv',mode='r')
    linea = file.readline() # skip the first line
    linea = file.readline()
    
    #vairables
    equipos = []
    visita,visitaganadores = [],[]
    local,localganadores = [],[]
    matriz = []
    l_wins,v_wins,tie = 0,0,0

    #lectura del archivo
    while linea:
        date,home_team,apponent_team,winner = linea[1:].split(',')
        
        #creo listas de equipos,locales,visitantes y ganadores
        if home_team not in equipos:
            añadiralista(equipos,home_team)
        if apponent_team not in equipos:
            añadiralista(equipos,apponent_team)
        añadiralista(visita,apponent_team)
        añadiralista(local,home_team)
        if home_team+"\n" == winner:
            añadiralista(localganadores,home_team)
        if apponent_team+"\n" == winner:
            añadiralista(visitaganadores,apponent_team)
        
        linea = file.readline()
    
    #creacion de matriz con los datos de los paises
    for elemento in equipos:
         añadiralista(matriz,winrate(elemento))
    
    # ordenar la matriz por el porcentaje de vicorias
    matriz = sorted(matriz, key=lambda x: x[-1], reverse=True)
    
    #informar de los equipos que ganaron mas de lo que perdieron
    print("PAISES ORDENADOS POR SU PORCENTAJE DE VICOTRIAS\n")
    for fila in matriz:
        if fila[-1] > 50:
            print(f"{fila[0]}: gano {fila[1]} de {fila[2]} partidos con un porcentaje de victorias de {fila[-1]:.2f}%\n")
    
    #informar si hubo mas victorias de local que de visita
    print("-"*133)
    print(f"De local hubo {len(localganadores)} vitorias, de visitante hubo {len(visitaganadores)}, la cantidad de partidos fue {len(localganadores)+len(visitaganadores)} y el porcentaje de  vitorias de local es de  {len(localganadores)*100/(len(localganadores)+len(visitaganadores)):.2f}")
    print("-"*133)
    print()
    
    #informar los equipos con mas victorias de local que de vistante
    print("PASIES CON MAS VICTORIAS DE LOCAL QUE DE VISITANTES\n")
    for fila in matriz:
        if fila[-3]>fila[-2]:
            print(f"{fila[0]} tiene {fila[-3]} victorias de local y {fila[-2]} de visitante\n")

except IOError:
    #Excepcion por si no se encuentra el archivo
    print('no se pudo crear el archivo')

finally:
    #Cierre del archivo
    file.close()

