atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 12, "Corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades":["Musculação", "Yoga", "Pilates"],
        "treinos": {"Musculação": 15, "Yoga":10, "Pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["Corrida", "Ciclismo"],
        "treinos":{"Corrida": 20, "Ciclismo": 18}
    }
]

def media_idade(atletas, esporte):
    soma_idades = 0
    qtd = 0
    for atleta in atletas:
        if esporte in atleta["modalidades"]:
            soma_idades += atleta["idade"]
            qtd += 1
    if qtd == 0:
        return 0
    return soma_idades / qtd

def esporte_mais_treinado(atletas, nome):
    for atleta in atletas:
        if atleta["nome"] == nome:
            treinos = atleta["treinos"]
            mais_treinado = None
            max_treinos = -1
            for esporte, qtd in treinos.items():
                if qtd > max_treinos:
                    mais_treinado = esporte
                    max_treinos = qtd
            return mais_treinado, max_treinos
    return None 

def atletas_multimodais(atletas):
    lista = []
    for atleta in atletas:
        if len(atleta["modalidades"]) > 2:
            lista.append(atleta["nome"])
    return lista

print("Média de idade (Natação):", media_idade(atletas, "Natação"))
print("Esporte mais treinado (Lucas):", esporte_mais_treinado(atletas, "Lucas"))
print("Atletas com mais de 2 modalidades:", atletas_multimodais(atletas))