# Pequena alteração para testar o Pull Request

def extract_movies(soup):
    movies_table = soup.find('table', attrs={'data-caller-name': 'chart-moviemeter'})

    if movies_table is None:
        print("Erro: Tabela de filmes não encontrada. O layout da página pode ter mudado.")
        return

    movies_table_body = movies_table.find('tbody')

    if movies_table_body is None:
        print("Erro: Corpo da tabela não encontrado.")
        return

    movies_table_rows = movies_table_body.find_all('tr')
    movie_links = ['https://imdb.com' + movie.find('a')['href'] for movie in movies_table_rows if movie.find('a')]

    if not movie_links:
        print("Nenhum link de filme encontrado.")
        return

    threads = min(MAX_THREADS, len(movie_links))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(extract_movie_details, movie_links)
