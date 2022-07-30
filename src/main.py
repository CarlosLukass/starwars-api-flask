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

# Flask_jwt_extended
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# Models
from models import db, Users, Characters, Species, Planets, Vehicles, Starships, Favorites_characters, Favorites_planets, Favorites_species, Favorites_vehicles, Favorites_starships

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')
MIGRATE = Migrate(app, db)

# Configurations
jwt = JWTManager(app)
db.init_app(app)
setup_admin(app)
CORS(app)


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

# Login  ====================================================================
@app.route("/login", methods=["POST"])
def login():
    user_email = request.json.get("email", None)
    user_password = request.json.get("password", None)

    user = Users.query.filter_by( email = user_email ).first()
    print(f"esto es: {user}")
    

    # Validations
    # If user send a empty field
    if user_email is None or user_password is None:
        return jsonify({"msg": "please send your email and password"}), 401

    if user is None:
        return jsonify({"msg": "wrong username or password, try again"}), 401
    else:
        if user_password != user.password:
            return jsonify({"msg": "wrong username or password, try again"}), 401

    access_token = create_access_token(identity=user_email)
    return jsonify(access_token=access_token)

    
# Register  ====================================================================
@app.route("/signup", methods=["POST"])
def signup():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    
    # Comprobations
    if email is None or password is None:
        return jsonify({"msg": "Bad email or password"}), 401

    new_user = Users(email = email, password = password, is_active = True)

    db.session.add(new_user)
    db.session.commit()

    body_response = {
        "msg": "User create successfully"
    }

    return body_response

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
@app.route('/favorites', methods=['GET'])
@jwt_required()
def handle_favorites():

    # GET
    if request.method == 'GET':
        current_user = get_jwt_identity()

        if current_user is None:
            return jsonify({"msg": "please login to see your favorites"}), 401

        user_data = Users.query.filter_by( email = current_user).first()
        print(user_data.id)

        fav_characters = Favorites_characters.query.filter_by( user_id = user_data.id ).all()
        fav_planets = Favorites_planets.query.filter_by( user_id = user_data.id ).all()
        fav_species = Favorites_species.query.filter_by( user_id = user_data.id ).all()
        fav_vehicles = Favorites_vehicles.query.filter_by( user_id = user_data.id ).all()
        fav_starships = Favorites_starships.query.filter_by( user_id = user_data.id ).all()

        results = {
            "characters": list(map(lambda item: item.serialize(), fav_characters)),
            "characters": list(map(lambda item: item.serialize(), fav_planets)),
            "characters": list(map(lambda item: item.serialize(), fav_species)),
            "characters": list(map(lambda item: item.serialize(), fav_vehicles)),
            "characters": list(map(lambda item: item.serialize(), fav_starships)),
        }

        response_body = {
            'status': int(Response().status_code),
            'results': results,
        }
        return jsonify(response_body), 200



######################################################
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
