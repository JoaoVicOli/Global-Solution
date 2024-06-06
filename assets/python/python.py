import random

conferir_ph = []
conferir_temperatura = []


def aleatorio(minimo, maximo):
    return round(random.uniform(minimo, maximo), 1)
i= 0

while i < 2:
    i+=1
    ph = aleatorio(1, 15)                                    
    temperatura = aleatorio(0, 30)
    if 7.8 <= ph or ph => 8.2:
        print(f"O ph está muito baixo: {ph}, resolver rápido")
        conferir_ph.append(ph)
        print(conferir_ph)
    else:
        print(f"O ph está aceitável: {ph}")

    if temperatura <= 10 or temperatura => 30:
        print("A temperatura está com problema, resolver rápido")
        conferir_temperatura.append(temperatura)
        print(conferir_temperatura)
    else:
        print("A temperatura está aceitável")