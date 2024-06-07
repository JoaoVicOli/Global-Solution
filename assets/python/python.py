import random

conferir_ph = []
conferir_temperatura = []

def aleatorio(minimo, maximo):
    return round(random.uniform(minimo, maximo), 1)

i = 0

while i < 2:
    i += 1
    
    for _ in range(3):  # Realizar 3 medições em cada iteração do while
        ph = aleatorio(1, 15)                                    
        temperatura = aleatorio(0, 30)
        
        # Verificação do pH
        if ph < 7.8 or ph > 8.2:
            print(f"O pH está fora do intervalo aceitável: {ph}, resolver rápido")
            conferir_ph.append(ph)
            print(f"Valores de pH fora do intervalo: {conferir_ph}")
        else:
            print(f"O pH está aceitável: {ph}")

        # Verificação da temperatura
        if temperatura <= 10 or temperatura > 30:
            print(f"A temperatura está fora do intervalo aceitável: {temperatura}, resolver rápido")
            conferir_temperatura.append(temperatura)
            print(f"Valores de temperatura fora do intervalo: {conferir_temperatura}")
        else:
            print(f"A temperatura está aceitável: {temperatura}")