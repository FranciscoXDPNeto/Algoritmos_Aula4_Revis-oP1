musicas = [
    {
        "titulo": "Back in Black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliacoes": [5, 4, 5, 5, 4, 5]
    },
     {
        "titulo": "Stairway to Heaven",
        "artista": "Led Zepplin",
        "downloads": 8900,
        "avaliacoes": [5, 5, 4, 5, 5, 5]
    }, {
        "titulo": "Enter Sandman",
        "artista": "Mettalica",
        "downloads": 8100,
        "avaliacoes": [5, 5, 5, 4, 4, 5, 5]
    }
]

def calcular_medias(musicas):
    medias = {}
    for musica in musicas:
        avaliacoes = musica["avaliacoes"]
        if len(avaliacoes) > 0:
            media = sum(avaliacoes) / len(avaliacoes)
        else:
            media = 0
        medias[musica["titulo"]] = round(media, 2)
    return medias

def artista_mais_downloads(musicas):
    downloads_artistas = {}
    for musica in musicas:
        artista = musica["artista"]
        if artista not in downloads_artistas:
            downloads_artistas[artista] = 0
        downloads_artistas[artista] += musica["downloads"]

    mais_baixado = None
    max_downloads = -1
    for artista, total in downloads_artistas.items():
        if total > max_downloads:
            mais_baixado = artista
            max_downloads = total
    return mais_baixado, max_downloads

def ranking_musicas(musicas):
    lista_medias = []
    for musica in musicas:
        avaliacoes = musica["avaliacoes"]
        if len(avaliacoes) > 0:
            media = sum(avaliacoes) / len(avaliacoes)
        else:
            media = 0
        lista_medias.append((musica["titulo"], round(media, 2)))

    ranking = sorted(lista_medias, key=lambda x: x[1], reverse=True)
    return ranking

print("Médias das músicas:", calcular_medias(musicas))
print("Artista com mais downloads:", artista_mais_downloads(musicas))
print("Ranking das músicas mais bem avaliadas:", ranking_musicas(musicas))