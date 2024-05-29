import random
temperatura = 0
aleatorio_ph = 10 * random.random()

ph = aleatorio_ph

conferir_ph = []
conferir_ph.append(ph)
conferir_temperatura = []


def random_with_one_decimal(min_value, max_value):
    return round(random.uniform(min_value, max_value), 1)

for i in range(10):
    i+=1
    print(random_with_one_decimal(5, 9))
    print(f"O ph está muito baixo: {ph:.1}")
    conferir_ph.append(ph)

if temperatura > 30:
    print("A temperatura está com problema")
    conferir_temperatura.append(temperatura)
