import bs4
import requests

# Un URL sin número de página
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

# Lista de títulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar páginas
for pagina in range(1, 51):

    # crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # selección de los datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # verificar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardando el título en una variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Ver lista de libros de 4 o 5 estrellas
for t in titulos_rating_alto:
    print(t)
