from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
import json

with open ('cities.json', encoding="utf8") as datos:
    data = datos.read()
cities = json.loads(data)

app = Flask(__name__)
CORS(app)


# ------------- Filter Data ----------------------
# Metods: GET
# Opcion para obtener los datos de ciudades registradas.
@cross_origin
@app.route('/search')
def home():
    return jsonify({"message": "Large cities in the US and Canada."},{"search": cities})


# Opcion para filtrar los datos por sugerencias.
@cross_origin
@app.route('/search/q=<parametros>', methods=['GET'])
def getCities(parametros):

    coincidences = []   # Vector de coincidencias
    scores = []
    results = []
    data = parametros.split('&')
    size = len(data)

    # Selección de datos:
    if size >= 2:
        name = data[0]
        latitude = data[1].split('=')
        longitude = data[2].split('=')
        lat = abs(float(latitude[1]))
        long = abs(float(longitude[1]))

        # Busqueda:
        for city in cities:
            if name in city["name"]:
                score1 = abs(((lat-abs(float(city["lat"])))))
                score2 = abs((long-abs(float(city["long"]))))
                score = (score1 + score2)/2
                scores.append(1) if score < 1 else scores.append(score)
                
                coincidences.append({'name' : city["name"],
                            'latitude' : city["lat"],
                            'longitude' : city["long"],
                            'score' : score        })
        scores.sort()
        #print(scores)    
        minimo = min(scores)
        maximo = max(scores)    

        for j in coincidences:
            j['score'] = 1 - (j['score'] * minimo / maximo)

        results = sorted(coincidences, key=lambda i: i['score'], reverse=True)

        # Muestra de coincidencias
        response = jsonify({"search": [ results ]})
        return response
    return notFound()


#----------------ERROR-----------------------
@cross_origin
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)