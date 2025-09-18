filmes = [
    {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "bilheteria": 830,
        "avaliacoes": [9, 10, 8, 9, 10]
    },
    {
        "titulo": "Avengers: Endgame",
        "diretor": "Anthony Russo",
        "bilheteria": 2797,
        "avaliacoes": [9, 9, 10, 10, 9]
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Christopher Nolan",
        "bilheteria": 1005,
        "avaliacoes": [10, 10, 9, 10, 10]
    },
    {
        "titulo": "Jurassic Park",
        "diretor": "Steven Spielberg",
        "bilheteria": 1029,
        "avaliacoes": [8, 9, 9, 8, 9]
    }
]

def top_bilheteria(filmes):
    ranking = sorted(filmes, key=lambda f: f["bilheteria"], reverse=True)
    return ranking[:3]

def top_avaliacao(filmes):
    medias = []
    for filme in filmes:
        avaliacoes = filme["avaliacoes"]
        media = sum(avaliacoes) / len(avaliacoes)
        medias.append((filme["titulo"], round(media, 2)))
    ranking = sorted(medias, key=lambda x: x[1], reverse=True)
    return ranking[:3]

def bilheteria_por_diretor(filmes):
    resultado = {}
    for filme in filmes:
        diretor = filme["diretor"]
        if diretor not in resultado:
            resultado[diretor] = 0
        resultado[diretor] += filme["bilheteria"]
    return resultado

def campeao(filmes):
    melhor_filme = None
    melhor_score = -1
    for filme in filmes:
        media_avaliacao = sum(filme["avaliacoes"]) / len(filme["avaliacoes"])
        score = filme["bilheteria"] * media_avaliacao
        if score > melhor_score:
            melhor_score = score
            melhor_filme = (filme["titulo"], round(media_avaliacao, 2), filme["bilheteria"])
    return melhor_filme

print("Top 3 bilheteiras:")
for f in top_bilheteria(filmes):
    print(f["titulo"], "-", f["bilheteria"], "milhões")

print("Top 3 avaliações:", top_avaliacao(filmes))
print("Bilheteria por diretor:", bilheteria_por_diretor(filmes))
print("Campeão absoluto:", campeao(filmes))