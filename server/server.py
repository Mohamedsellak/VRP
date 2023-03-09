from flask import Flask, request, jsonify
from flask_cors import CORS
from optimalpath import *
from folium_map import folium_map


app = Flask(__name__)
CORS(app)
@app.route('/', methods = ['POST','GET'])
def search():
    # recuperer les location a partir de Leaflet js Map
    data = request.get_json()
    # convert array of json object to array of tuples
    data = [tuple(d.values()) for d in data['locations']]
    # set the default optimal route solution 
    route = [index for index in range(len(data))]
    # calcule the distance of the solution 
    distance = total_distance(route, data)


    for i in range(1,len(route)):
        for j in range(1,len(route)):
            swap(route,i,j)
            new_distance = total_distance(route, data)
            if new_distance < distance :
                distance = new_distance

    newdata = [ data[i] for i in route]
    newdata.append(newdata[0])

    # folium_map(newdata)

    return jsonify(newdata)

if __name__ == '__main__':
    app.run()