# chilean-artists-python-spotipy-webscraping
## Primer acercamiento a Python

Siempre quise saber cuáles eran las canciones chilenas más escuchadas en Spotify. 
Investigando, encontré una librería en Python llamada [Spotipy](https://spotipy.readthedocs.io/), para obtener datos de Spotify. Sin embargo, con esta librería no es posible obtener los artistas o canciones según un determinado país. Así que se me ocurrió contruir una lista de artistas chilenos, extrayendo información con web scraping, desde una pagina que tiene el mejor catalogo (según yo) de artistas chilenos: [Musica Popular](https://www.musicapopular.cl/), y con eso podría utilizar la librería.  

Lamentablemente tuve varios inconvenientes. Como por ejemplo:
- Al buscar por un artista "X", la librería devuelve varios artistas que coincidan con ese nombre, entonces ¿Cual elijo?. 
- Los artistas que calzaban con el nombre específico no necesariamente eran chilenos. 
- El campo popularidad es un numero que puede variar con el tiempo (por lo que entendi), así que si fue un hits en los 80, hoy tal vez ya no (en ese caso me hubiese gustado tener algun campo "nro de reproducciones".

Teniendo los datos relativamente limpios (tuve que hacer mucha limpieza manual), con SpotiPy tambien se pueden crear playlist, así que creé Playlist en Spotify con las 100 canciones chilenas más populares de cáda década. 

Si estas leyendo esto y quieres ver como quedó, busca en spotify las playlist: "Top Chile " + la decada (80,90,00). 

## Librerías:

* [Spotipy](https://spotipy.readthedocs.io/) - Spotipy is a lightweight Python library for the Spotify Web API 
* [Pandas](https://pandas.pydata.org/) - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool.
* [Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites.



