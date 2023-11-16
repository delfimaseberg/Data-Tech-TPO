def añadiralista(lista,elemento):
    #añade elementos a una lista
    lista.append(elemento)
    return lista

def winrate(elemento,visita,visitaganadores,local,localganadores):
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

def procesar():
        #Apertura del archivo
        file = open(r'C:\Users\Delfina\Documents\algoritmos y estructuras de datos\tp entrega\penality kick.csv',mode='r')
        linea = file.readline() # skip the first line
        linea = file.readline()
        
        #vairables
        equipos = []
        visita,visitaganadores = [],[]
        local,localganadores = [],[]
        matriz = []

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
            
        return equipos,visita,visitaganadores,local,localganadores,matriz,file

def main():
    try:
        #variables
        equipos,visita,visitaganadores,local,localganadores,matriz,file = procesar()
        
        #creacion de matriz con los datos de los paises
        for elemento in equipos:
            añadiralista(matriz,winrate(elemento,visita,visitaganadores,local,localganadores))
        
        #ordenar la matriz por el porcentaje de vicorias
        matriz = sorted(matriz, key=lambda x: x[-1], reverse=True)
        
        a = f"De local hubo {len(localganadores)} vitorias, de visitante hubo {len(visitaganadores)}, la cantidad de partidos fue {len(localganadores)+len(visitaganadores)} y el porcentaje de  vitorias de local es de  {len(localganadores)*100/(len(localganadores)+len(visitaganadores)):.2f}"
        #informar los paises con mas victorias y ordenados de tal manera
        print("-"*len(a))
        print("PAISES ORDENADOS POR SU PORCENTAJE DE VICTORIAS")
        print("{:<23} {:<10} {:<10} {:<10}".format("PAIS", "VICTORIAS", "PARTIDOS", "PORCENTAJE"))
        for fila in matriz:
            if fila[-1] > 50:
                print("{:<23} {:<10} {:<10} {:<10.2f}%".format(fila[0], fila[1], fila[2], fila[-1]))
        print("-"*len(a))
        
        #informar los equipos con mas victorias de local que de vistante
        print("PASIES CON MAS VICTORIAS DE LOCAL QUE DE VISITANTES")
        print("{:<24} {:<18} {:<20}".format("PAIS", "VICTORIAS LOCAL", "VICTORIAS VISITANTE"))
        for fila in matriz:
            if fila[-3]>fila[-2]:
                print("{:<24} {:<18} {:<20}".format(fila[0], fila[1], fila[2]))
                
        #informar si hubo mas victorias de local que de visita
        print("-"*len(a))
        print(a)
        print("-"*len(a))
                
    except IOError:
        #Excepcion por si no se encuentra el archivo
        print('no se pudo crear el archivo')

    finally:
        #Cierre del archivo
        file.close()

if __name__ == "__main__":
    main()