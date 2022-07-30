"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, Response, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Characters, Species, Planets, Vehicles, Starships, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Users ========================================================================
@app.route('/users', methods=['GET'])
def handle_users():

    # GET
    if request.method == 'GET':
        users = Users.query.all()
        total_users = len(users)
        results = list(map(lambda user:user.serialize(), users))
        response_body = {
            'status': int(Response().status_code),
            'total_users': total_users,
            'results': results
        }
        return jsonify(response_body), 200

# Users by ID
@app.route('/users/<int:id>', methods=['GET'])
def handle_users_by_id(id):
    
    # GET
    if request.method == 'GET':
        user = Users.query.get(id)
        result = user.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Characters  ====================================================================
@app.route('/characters', methods=['GET'])
def handle_characters():
    
    # GET
    if request.method == 'GET':
        characters = Characters.query.all()
        total_characters = len(characters)
        results = list(map(lambda character:character.serialize(), characters))
        response_body = {
            'status': int(Response().status_code),
            'total_characters': total_characters,
            'results': results
        }
        return jsonify(response_body), 200

# Character by ID
@app.route('/characters/<int:id>', methods=['GET'])
def handle_characters_by_id(id):
    
    # GET
    if request.method == 'GET':
        character = Characters.query.get(id)
        result = character.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Species ======================================================================
@app.route('/species', methods=['GET'])
def handle_species():
    
    # GET
    if request.method == 'GET':
        species = Species.query.all()
        total_species = len(species)
        results = list(map(lambda specie: specie.serialize(), species))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_species': total_species
        }
        return jsonify(response_body), 200

# Specie by ID
@app.route('/species/<int:id>', methods=['GET'])
def handle_species_by_id(id):
    
    # GET
    if request.method == 'GET':
        specie = Species.query.get(id)
        result = specie.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Planets ======================================================================
@app.route('/planets', methods=['GET'])
def handle_planets():
    
    # GET
    if request.method == 'GET':
        planets = Planets.query.all()
        total_planets = len(planets)
        results = list(map(lambda planet:planet.serialize(), planets))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_planets': total_planets
        }
        return jsonify(response_body), 200

# Planet by ID
@app.route('/planets/<int:id>', methods=['GET'])
def handle_planets_by_id(id):
    
    # GET
    if request.method == 'GET':
        planet = Planets.query.get(id)
        result = planet.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Vehicles ======================================================================
@app.route('/vehicles', methods=['GET'])
def handle_vehicles():

    # GET
    if request.method == 'GET':
        vehicles = Vehicles.query.all()
        total_vehicles = len(vehicles)
        results = list(map(lambda vehicle:vehicle.serialize(), vehicles))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_vehicles': total_vehicles
        }
        return jsonify(response_body), 200

# Vehicle by ID
@app.route('/vehicles/<int:id>', methods=['GET'])
def handle_vehicles_by_id(id):

    # GET
    if request.method == 'GET':
        vehicle = Vehicles.query.get(id)
        result = vehicle.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Starships ======================================================================
@app.route('/starships', methods=['GET'])
def handle_starships():

    # GET
    if request.method == 'GET':
        starships = Starships.query.all()
        total_starships = len(starships)
        results = list(map(lambda starship:starship.serialize(), starships))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_vehicles': total_starships
        }
        return jsonify(response_body), 200

# Starship by ID
@app.route('/starships/<int:id>', methods=['GET'])
def handle_starships_by_id(id):

    # GET
    if request.method == 'GET':
        starship = Starships.query.get(id)
        result = starship.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Favorites ======================================================================
@app.route('/favorites/<int:user_id>', methods=['GET'])
def handle_favorites(user_id):

    # GET
    if request.method == 'GET':
        favorites = Favorites.query.filter_by( user_id = user_id )
        results = list(map(lambda favorite:favorite.serialize(), favorites))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
        }
        return jsonify(response_body), 200

# Add new favorite
@app.route('/favorites/<category>/<int:id>', methods=['POST', 'DELETE'])
def handle_add_new_favorites(category,id):
        
    # POST
    if response.method == 'POST':
        body = request.get_json()
        user_id = User.query.get(body['user_id'])

        if category == 'characters':
            new_favorite = Favorites( characters_id = body[f"{category}_{id}"], user_id = body['user_id'])
        if category == 'species':
            new_favorite = Favorites( species_id = body[f"{category}_{id}"], user_id = body['user_id'])
        if category == 'planets':
            new_favorite = Favorites( planets_id = body[f"{category}_{id}"], user_id = body['user_id'])
        if category == 'vehicles':
            new_favorite = Favorites( vehicles_id = body[f"{category}_{id}"], user_id = body['user_id'])
        if category == 'starships':
            new_favorite = Favorites( starships_id = body[f"{category}_{id}"], user_id = body['user_id'])

        db.session.add(new_favorite)
        db.session.commit()
        
        response_body = {
            'results': new_favorite.serialize()
        }
        return jsonify(response_body), 200
        
        # DELETE
        if response.method == 'DELETE':
            body = request.get_json()

            if category == 'characters':
                row = Favorites.query.filter_by(characters_id = body[f"{category}_{id}"], user_id = body['user_id'])
            if category == 'species':
                row = Favorites.query.filter_by(species_id = body[f"{category}_{id}"], user_id = body['user_id'])
            if category == 'planets':
                row = Favorites.query.filter_by(planets_id = body[f"{category}_{id}"], user_id = body['user_id'])
            if category == 'vehicles':
                row = Favorites.query.filter_by(vehicles_id = body[f"{category}_{id}"], user_id = body['user_id'])
            if category == 'starships':
                row = Favorites.query.filter_by(starships_id = body[f"{category}_{id}"], user_id = body['user_id'])

        session.delete(row)
        session.commit()

        response_body = {
            'results': 'record deleted successfully'
        }
        return jsonify(response_body), 200

        
        

######################################################
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
