from sklearn.neighbors import KNeighborsClassifier

# temperatura, umidade, vento e resultado

cenarios = [
    [22, 66, 15, 1],
    [30, 20, 18, 0],
    [20, 90, 20, 1],
    [33, 25, 5, 0],
    [28, 36, 12, 0],
    [12, 60, 15, 1],
    [16, 90, 18, 1],


]

maquina = KNeighborsClassifier(n_neighbors=3)

atributos = [cenario[:-1] for cenario in cenarios]
resultados = [cenario[-1] for cenario in cenarios]

maquina.fit(atributos, resultados)

# temperatura, umidade, vento
testes = [
    [18, 80, 20],
    [35, 10, 7]
]

predicoes = maquina.predict(testes)

cont = 0
for predicao in predicoes:
    if predicao == 1:
        predicao = "chuva"
    else:
        predicao = "sem chuva"
    print(f"Cenário {cont+1}: {predicao}")
    cont += 1

