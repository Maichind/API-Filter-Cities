# API - sugerencias de autocompletado para grandes ciudades de EE. UU. y Canadá.

## Funcionamiento:
- Para iniciar la API se ejecuta desde la terminal el comando: python main.py  
- Su ruta principal muestra todos los datos almacenados y para filtrar se deben enviar parámetros de nombre, latitud y longitud que se quieren filtrar separados por '&'.  
- Algunos ejemplos de rutas para filtrado son: http://127.0.0.1:9999/search/q=Green&latitude=45.98345&longitude=-65.89879, http://127.0.0.1:9999/search/q=Palm&latitude=30.68345&longitude=-79.59879, http://127.0.0.1:9999/search/q=Hall&latitude=37.38345&longitude=-75.22879, estas direcciones tienen primeramente un dato de nombre parcial, luego los datos de latitud y longitud correspondiente a lo que la API responderá con las sugerencias incluidas dentro de su base de datos.  
- El despliegue de la API se puede ver y usar en el siguiente enlace: https://api-filter-cities.onrender.com/search, de igual forma se pueden usar los datos de las peticiones en local u otros y corroborar el correcto funcionamiento: https://api-filter-cities.onrender.com/search/q=Green&latitude=45.98345&longitude=-65.89879.
