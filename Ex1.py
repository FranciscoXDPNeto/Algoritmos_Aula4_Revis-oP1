pedidos = [
    {
        "cliente": "Ana",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de laranja", "preco": 8}
        ]
    },
    {
        "cliente": "Bruno",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Refrigerante", "preco": 6},
            {"prato": "Sobremesa", "preco": 12}
        ]
    },
    {
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Suco de laranja", "preco": 8}
        ]
    },
]

def total_gasto_cliente(pedidos, nome_cliente):
    total = 0
    for pedido in pedidos:
        if pedido["cliente"] == nome_cliente:
            total += sum(item["preco"] for item in pedido["itens"])
    return total

def prato_mais_vendido(pedidos):
    contador = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            if prato not in contador:
                contador[prato] = 0
            contador[prato] += 1
    mais_vendido = None
    maior_qtd = 0
    for prato, qtd in contador.items():
        if qtd > maior_qtd:
            mais_vendido = prato
            maior_qtd = qtd
    return mais_vendido, maior_qtd

def ranking_clientes(pedidos):
    gastos = {}
    for pedido in pedidos:
        cliente = pedido["cliente"]
        if cliente not in gastos:
            gastos[cliente] = 0
        for item in pedido["itens"]:
            gastos[cliente] += item["preco"]
    ranking = sorted(gastos.items(), key=lambda x: x[1], reverse=True)
    return ranking[:3]

print("Total gasto pela Ana:", total_gasto_cliente(pedidos, "Ana"))
print("Prato mais vendido:", prato_mais_vendido(pedidos))
print("Ranking dos clientes:", ranking_clientes(pedidos))