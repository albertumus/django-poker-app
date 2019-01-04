from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import ComprobadorPoker, NumeroJugadores




# Create your views here.

def home(request):

    numero_jugadores_form = NumeroJugadores()

    if request.method == "POST":

        jugadores = NumeroJugadores(data=request.POST)
        jugadores = request.POST.get('numero_jugadores')
        print(jugadores)
        return redirect(reverse('comprobar')+'?{}'.format(jugadores))

    return render(request, 'core/home.html', {'form':NumeroJugadores})

def comprobacion(request):

    comprobrador_form = ComprobadorPoker()

    numero_jugadores = request.GET
    numero_jugadores = int(list(numero_jugadores.keys())[0])


    if request.method == "POST":

        jugadas_jugadores_mano = {}
        

        cartas = ComprobadorPoker(data=request.POST)

        #Parseo de Cartas por Jugador
        cartas1 = request.POST.getlist("carta1")
        palos1 = request.POST.getlist("palo1")
        cartas2 = request.POST.getlist("carta2")
        palos2 = request.POST.getlist("palo2")
        cartas3 = request.POST.getlist("carta3")
        palos3 = request.POST.getlist("palo3")
        cartas4 = request.POST.getlist("carta4")
        palos4 = request.POST.getlist("palo4")
        cartas5 = request.POST.getlist("carta5")
        palos5 = request.POST.getlist("palo5")
        ejemplo = request.POST.getlist("ejemplo")
    

        for jugador in range(0,numero_jugadores):
            jugadas_jugadores_mano['Jugador {}'.format(jugador+1)] = [[int(cartas1[jugador]),palos1[jugador]],[int(cartas2[jugador]),palos2[jugador]],[int(cartas3[jugador]),palos3[jugador]],[int(cartas4[jugador]),palos4[jugador]],[int(cartas5[jugador]),palos5[jugador]]]

        print(jugadas_jugadores_mano)

        #Script Importado

        """
        Hacer una lista con lsitas o diccionarios dentro. 
        Created on Tue Feb 20 17:43:21 2018
        asdasdasd
        @author: admin
        """

        from collections import Counter

        ############ FUNCIONES #####################
        #aqui se saca finalmente la mejor jugada de todas, para compararla con el resto de 
        #jugadores y saber quien gana
        def mejor_jugadas(nombre, mano):
            mejor_jugada = []
            resultado = jugadas()
            if resultado["escalera real"][0] == 1:
                mejor_jugada.append("escalera real")
                mejor_jugada.append(resultado["escalera real"][1])
            elif resultado["escalera de color"][0] == 1:
                mejor_jugada.append("escalera de color")
                mejor_jugada.append(resultado["escalera de color"][1])
            elif resultado["poker"][0] == 1:
                mejor_jugada.append("poker")
                mejor_jugada.append(resultado["poker"][1])
            elif resultado["full"][0] == 1:
                mejor_jugada.append("full")
                mejor_jugada.append(resultado["full"][1])
            elif resultado["color"][0] == 1:
                mejor_jugada.append("color")
                mejor_jugada.append(resultado["color"][1])
            elif resultado["escalera"][0] == 1:
                mejor_jugada.append("escalera")
                mejor_jugada.append(resultado["escalera"][1])
            elif resultado["trios"][0] == 1:
                mejor_jugada.append("trio")
                mejor_jugada.append(resultado["trios"][1])
            elif resultado["doble parejas"][0] == 1:
                mejor_jugada.append("doble pareja")
                mejor_jugada.append(resultado["doble parejas"][1])
            elif resultado["parejas"][0] == 1:
                mejor_jugada.append("pareja")
                mejor_jugada.append(resultado["parejas"][1])
            else:
                mejor_jugada.append("nada")
            return mejor_jugada
            
        #aqui saco las jugadas y obtengo un diccionario para luego sacar que jugada es mejor
        def jugadas():
            numeros_mano = obtener_repeticiones(mano)
            resultado = {}
            resultado["parejas"] = pareja(numeros_mano)
            resultado["trios"] = trio(numeros_mano)
            resultado["doble parejas"] = doble_parejas(numeros_mano)
            resultado["poker"] = poker(numeros_mano)
            resultado["full"] = full(numeros_mano)
            resultado["escalera"] = escalera_(mano)
            resultado["escalera de color"] = escalera_color(mano)
            resultado["color"] = color(mano)
            resultado["escalera real"] = escalera_real(mano)
            #retorna el diccionario llamado resultado
            return resultado
        #funcion para obtener el numero de repeticiones de cada carta 
        def obtener_repeticiones(mano):
            numeros_mano = []
            #recorre las cartas con su numero y palo
            for numero,palo in mano:
                #añade los numeros a una lista
                numeros_mano.append(numero)
                #la lista se pasa a diccionario donde estaŕa numero y repeticiones
            numeros_mano = Counter(numeros_mano)
            return numeros_mano
        #funcion que comprueba que todas las cartas son del mismo palo
        def comprobar_color(mano):
            #sacamos la lista a un palo
            palos = []
            #condicion de escalera de color
            c_escalera_color = 0
            #llenamos la lista palos para tenerlos todos
            for numero, palo in mano:
                palos.append(palo)
            #recorremos la lista palos para saber si todos los palos son los mismos
            for x in range(1,5):
                #de esta manera podemos saber cual era el anterior palo
                last = palos[x-1]
                #asi comprobamos que el palo actual es igual que el anterior
                if palos[x] == last:
                    #si es así la condición de escalera color aumenta en 1
                    c_escalera_color += 1 
                #si escalera de color es igual a 4 entonces la condición se habra cumplido
            return c_escalera_color       
        #funcion de escalera
        def escalera_(mano):
            numeros_mano_escalera = []
            escalera = 0
            for numero,palo in mano:
                numeros_mano_escalera.append(numero)
            numeros_mano_escalera.sort()
            #comprueba el numero
            c_escalera = comprobar_escalera(numeros_mano_escalera)
            if c_escalera == 4:
                escalera += 1
            return escalera, numeros_mano_escalera
        #comprueba si hay escalera y retorna el numero de cartas que son consecutivas
        def comprobar_escalera(numeros_mano_escalera):
                #si c_escalera = 4 signigica que 5 cartas son consecutivas
                c_escalera = 0
                #un bucle que va de 1 a 5
                for x in range(1,5):
                    #para saber el ultimo numero sacamos la posición de la lista y le sumamos 1
                    last = numeros_mano_escalera[x-1]+1
                    #si se cumple la condición se suma 1
                    if numeros_mano_escalera[x] == last:
                        c_escalera += 1
                return c_escalera
        #comprueba la jugada de color
        def color(mano):
            cartas = []
            for numero, palo in mano:
                cartas.append(numero)
            color = 0
            c_color = comprobar_color(mano)
            if c_color == 4:
                color += 1
            return color, cartas
        #funcion para comprobar escalera de color
        def escalera_color(mano):
            cartas = []
            for numero, palo in mano:
                cartas.append(numero)
            n_m_e = escalera_(mano)
            numeros_mano_escalera = n_m_e[1]
            escalera_color = 0
            escalera = comprobar_escalera(numeros_mano_escalera)
            if escalera == 4:
                c_escalera = comprobar_color(mano)
                if c_escalera == 4:
                    escalera_color += 1 
            return escalera_color, cartas
        #funcion de pareja 
        def pareja(numeros_mano):
            parejas = 0
            parejas_de = []
            for numero,repeticiones_numero in numeros_mano.items():
                #el bucle recorre el diccionario y saca numerosy sus repeticiones
                if repeticiones_numero == 2:
                    #si algun repetición coincide que es igual a 2 = pareja
                    parejas += 1
                    parejas_de.append(numero)
            return parejas, parejas_de
        #funcion de trio
        def trio(numeros_mano):
            trios = 0
            trios_de = []
            for numero, repeticiones_numero in numeros_mano.items():
                #el bucle recorre el diccionario y saca numerosy sus repeticiones
                if repeticiones_numero == 3:
                    trios += 1
                    trios_de.append(numero)
            return trios, trios_de

        def doble_parejas(numeros_mano):
            #pasamos la funcion de parejas para obtener las parejas 
            parejas = pareja(numeros_mano)
            #el numero de parejas
            numero_parejas = parejas[0]
            doble_parejas = 0
            doble_parejas_de = parejas[1]    
            if numero_parejas == 2:
                #si el numero de parejas coincide, añadimos 1 a doble pareja
                doble_parejas += 1
            return doble_parejas, doble_parejas_de
        #funcion de poker
        def poker(numeros_mano):
            poker = 0
            poker_de = []
            for numero, repeticiones_numero in numeros_mano.items():
                #el bucle recorre el diccionario y saca numerosy sus repeticiones
                if repeticiones_numero == 4:
                    poker += 1
                    poker_de.append(numero)
            return poker, poker_de
        #funcion de full 
        def full(numeros_mano):
            full = 0
            full_de = []
            parejas = pareja(numeros_mano)
            numero_parejas = parejas[0]
            pareja_de = parejas[1]
            trios = trio(numeros_mano)
            numero_trios = trios[0]
            trio_de = trios[1]
            if numero_parejas == 1 and numero_trios == 1:
                full += 1
                full_de.append(pareja_de)
                full_de.append(trio_de)
            return full, full_de
        #comprueba si hay una escalera real de color:
        def escalera_real(mano):
            escalera_real = 0
            c_escalera_real = 0
            numeros = []
            palos = []
            for numero, palo in mano:
                numeros.append(numero)
                palos.append("palo")
            if 1 in numeros and 10 in numeros and 11 in numeros and 12 in numeros and 13 in numeros:
                for x in range(1,5):
                    last = palos[x-1]
                    if palos[x] == last:
                        c_escalera_real += 1
            if c_escalera_real == 4:
                escalera_real += 1
            return escalera_real, numeros

                
        ###########################################
                
        jugadas_finales = {}

        for nombre,mano in jugadas_jugadores_mano.items():
            jugadas_finales[nombre] = mejor_jugadas(nombre,mano)

        print(jugadas_finales)

        resolucion = {}
        numeros_de_jugada = []

        for nombre, mano in jugadas_finales.items():
            if "escalera real" in mano: 
                resolucion.update({nombre: 9})
                numeros_de_jugada.append(8)
            if "escalera de color" in mano: 
                resolucion.update({nombre: 8})
                numeros_de_jugada.append(8)
            if "poker" in mano: 
                resolucion.update({nombre: 7})
                numeros_de_jugada.append(7)
            if "full" in mano: 
                resolucion.update({nombre: 6})
                numeros_de_jugada.append(6)
            if "color" in mano: 
                resolucion.update({nombre: 5})
                numeros_de_jugada.append(5)
            if "escalera" in mano: 
                resolucion.update({nombre: 4})
                numeros_de_jugada.append(4)
            if "trio" in mano: 
                resolucion.update({nombre: 3})
                numeros_de_jugada.append(3)
            if "doble pareja" in mano: 
                resolucion.update({nombre: 3})
                numeros_de_jugada.append(3)
            if "pareja" in mano: 
                resolucion.update({nombre: 2})
                numeros_de_jugada.append(2)
            if "nada" in mano:
                resolucion.update({nombre:1})
                numeros_de_jugada.append(1)

        numero_ganador = max(numeros_de_jugada)
                
        def resultado_final1 ():
            for mano in resolucion.items():
                if  mano[1] == numero_ganador:
                        return mano[0]

        def resultado_final2 ():
            z = {}
            for x,y in resolucion.items():
                if y == numero_ganador:
                    c = jugadas_finales[x][1]
                    z.update({x:c})
                else:
                    continue
            p = []
            for x,c in z.items():
                o = max(c)
                p.append(o)
            i = max(p)
            for x,c in z.items():
                if max(c) == i:
                    return x
            
            
        def core_final():
            ganadores = 0
            for numero in numeros_de_jugada:
                if numero == numero_ganador: 
                    ganadores += 1
                else: 
                    ganadores += 0
            if ganadores == 1:
                ganador = resultado_final1()
                return ganador
            if ganadores != 1 and ganadores != 0:
                ganador = resultado_final2()
                return ganador

        ganador = core_final()
        mejor_jugada_ganador = jugadas_finales[ganador][0]
        print(mejor_jugada_ganador)
        print(ganador)


    
        #Retorno de la pagina con los resultados
        return render(request, 'core/comprobacion.html', {'form':comprobrador_form,  'jugadores':range(1,numero_jugadores+1),'ganador':ganador,'mejor_jugada_ganador':mejor_jugada_ganador})

    return render(request, 'core/comprobacion.html', {'form':comprobrador_form, 'jugadores':range(1,numero_jugadores+1)})