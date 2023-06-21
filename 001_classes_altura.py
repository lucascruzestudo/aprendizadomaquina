from sklearn.tree import DecisionTreeClassifier

def obter_classe(previsao):
    if previsao == 0:
        return "Baixa"
    elif previsao == 1:
        return "Média"
    elif previsao == 2:
        return "Alta"

base_alturas = [
    [155,0],
    [160,0],
    [175,1],
    [180,2],
    [170,1],
    [179,1],
    [190,2],
    [149,0],
    [174,1],
    [185,1]
]

alturas = [[dado[0]] for dado in base_alturas]
classes = [[dado[1]] for dado in base_alturas]

modelo = DecisionTreeClassifier()
modelo.fit(alturas,classes)

while True:
    try:
        altura = [[int(input("Informe a altura: "))]]
        previsao = modelo.predict(altura)
        resultado = obter_classe(previsao)
        print(resultado)
    except:
        print("ERRO: Valor inválido\n")
